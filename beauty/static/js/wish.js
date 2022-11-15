//wishlist 

let wishIcon=document.querySelector('#love-icon');
let wish=document.querySelector('.wishList');
let closewish=document.querySelector('#close-love');

wishIcon.onclick = () => {
    wish.classList.add("actived");
}; 

closewish.onclick = () => {
    wish.classList.remove("actived");
};
console.log("maha world!");