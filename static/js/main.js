let visible = 8
const postsBox = document.getElementById('posts_box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')

const handleGetData = () =>{
    $.ajax({
        type: 'GET',
        url: `/posts-json/${visible}/`,
        success: function(response){
            //console.log(response.max)
            maxSize = response.max            
            const data = response.data 
            spinnerBox.classList.remove('not-visible')
            setTimeout(()=>{
                spinnerBox.classList.remove('not-visible')
                data.map(post=>{
                    console.log(post.meme_id)
                    postsBox.innerHTML += `<div class="card p-3 mt-3 mb-3">
                                                ${post.title}
                                                <br>
                                                ${post.price}
                                            </div>`
                })
            }, 500)
            
            if(maxSize){
                console.log('done')
                loadBox.innerHTML = "<h4>No more memes to load :(</h4"
            }
        },
        error: function(error){
            console.log(error)
        }
    })
}

handleGetData()

loadBtn.addEventListener('click', ()=>{
    visible += 6
    handleGetData()
})