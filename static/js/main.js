document.querySelector('.btn2').style.display = 'none';
document.querySelector('btn1.').addEventListener('click', showBtn);

function showBtn(e){
    document.querySelector('.btn2').style.display='block';
    e.preventDefault()
}