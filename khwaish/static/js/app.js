searchbox = document.getElementById('txtsearch');

searchbox.addEventListener('keyup', search);

async function fetchdata(url) {

    const result = await fetch(url);

    const data = await result.json();

    return data;

}

function search() {
    var div = document.createElement('div');
    var ul = document.createElement('ul');
    var divresult = document.getElementById('result');
    val = searchbox.value;

    if (val == '') {
        window.location = '';
    }
    else {
//        fetchdata(`search/${val}`)
          fetchdata(`http://127.0.0.1:8000/search/${val}/`)
            .then(function (data) {
                console.log(data);
                for (var i = 0; i < data.length; i++) {
                    var imgdiv = document.createElement('div');
                    var img = document.createElement('img');
                    var li = document.createElement('li');
                    var a = document.createElement('a');


                    a.href = `http://127.0.0.1:8000/artist/painting/${data[i]['pk']}`;
                    a.text = data[i]['fields']['paintingname'];

                    imgdiv.text = data[i]['fields']['paintingimage'];

                    img.src = `http://127.0.0.1:8000/Media/${data[i]['fields']['paintingimage']}`;
                    img.style.height = '50px';
                    img.style.width = '50px';

                    li.style.marginBottom = '5px';


                    li.appendChild(img);
                    li.appendChild(a);


                    ul.appendChild(li);
                    div.appendChild(ul);

                    divresult.className = 'searchbox';
                    divresult.appendChild(div);

                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }



}




// divresult.style.display = block;
//                     divresult.innerHTML += `<ul>
//                          <li>${data[i]['fields']['paintingname']}</li>
//                     // </ul>


// a.href = `artist/painting/${data[i]['pk']}`;
// var textdata = document.createTextNode(data[i]['fields']['paintingname']);
// li.appendChild(textdata);
// console.log(a);
// li.appendChild(a)
// ul.appendChild(li);
// div.appendChild(ul);
// div.className = 'searchbox';
// divresult.appendChild(div);