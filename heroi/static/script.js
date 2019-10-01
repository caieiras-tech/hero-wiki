let heroi = document.querySelector('.heroi');
let det = document.querySelector('.detalhes');

heroi.onmouseover =()=>{
    det.style.display = 'flex';
}

heroi.onmouseout =()=>{
    det.style.display = 'none';
}