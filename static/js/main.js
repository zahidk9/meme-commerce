const postsBox = document.getElementById('posts-box')
console.log(postsBox)
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
let visible = 6

const handleDataRetrieval = () => {
    $.ajax({
        type: 'GET',
        url: `/posts-json/${visible}`,
        success: function(response){
            maxSize = response.max 
            const data = response.data
            spinnerBox.classList.remove('not-visible')
            setTimeout(()=>{
                spinnerBox.classList.add('not-visible')
                data.map(post=>{
                    console.log(post.id)
                    postsBox.innerHTML += `<div class="card p-3 mt-3 mb-3">
                                                ${post.name}
                                                <br>
                                                ${post.body}
                                            </div>`
                })
                if(maxSize){
                    console.log('done')
                    loadBox.innerHTML = "<h4>No more memes to load :(</h4>"
                }
            }, 500)
        },
        error: function(error){
            console.log(error)
        }
    })
}

handleDataRetrieval()

loadBtn.addEventListener('click', ()=>{
    visible += 6
    handleDataRetrieval()
})