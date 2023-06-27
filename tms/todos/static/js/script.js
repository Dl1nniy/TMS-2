function myFunction() {
        alert("task completed");
};

window.onload = function() {
    console.log('документ загружен');

    document.getElementById('button').addEventListener('click', myFunction);
};



