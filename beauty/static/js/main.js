//cart 
let cartIcon=document.querySelector('#cart-icon');
let cart=document.querySelector('.cart');
let closeCart=document.querySelector('#close-cart');

cartIcon.onclick = () => {
    cart.classList.add("active");
}; 

closeCart.onclick = () => {
    cart.classList.remove("active");
};

console.log("hello world");



//navbar
const bar = document.getElementById('bar');
const close = document.getElementById('close');
const nav = document.getElementById('navbar');

if (bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}

if (close) {
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}
//cart working
if (document.readyState == "loading")   {
    document.addEventListener('DOMContentLoaded',ready);
} else {
    ready();
}



function ready() {
    //remove item from cart
    var removeCartbutton=document.getElementsByClassName('cart-remove');
    console.log(removeCartbutton);
    for ( var i = 0; i < removeCartbutton.length; i++){
        var button=removeCartbutton[i];
        button.addEventListener("click", removeCartItem);
    }
    //quantity changes
    var quantityInputs=document.getElementsByClassName('cart-quantity')
    for( var i = 0; i < quantityInputs.length; i++){
        var input=quantityInputs[i];
        input.addEventListener("change",quantityChanged)
    }
    var addCart = document.getElementsByClassName('add-cart');
    for( var i = 0; i < addCart.length; i++){
        var button=addCart[i];
        button.addEventListener("click", addCartClicked)
    }
    document.getElementsByClassName('btn-buy').addEventListener("click", buybuttonClicked);
}

function buybuttonClicked(){
    alert("Your Order Is Bleased");
    var cartcontent=document.getElementsByClassName('cart-content')[0];
    while(cartcontent.hasChildNodes()){
        cartcontent.removeChild(cartcontent.firstChild);
    }
    updatetotal();
}


function removeCartItem(event){
    var buttonCliked=event.target;
    buttonCliked.parentElement.remove();
    updatetotal();

}
function quantityChanged(event){
    var input =event.target;
    if(isNaN(input.value) || input.value <= 0){
        input.value=1;
    }
    updatetotal();
}


// add to cart
function addCartClicked(event){
    var button=event.target;
    var shopProduct = button.parentElement;
    var titleObj = shopProduct.querySelector('.product-title')
    var id = titleObj.dataset.id;
    var title=titleObj.innerText;
    var price=shopProduct.querySelector('.price').innerText;
    console.log(shopProduct.querySelector('.price'))
    var productImg=document.querySelector('.product-img').src;
    addProductToCart(title,price,productImg, id)
    updatetotal();
}
function addProductToCart(title,price,productImg, id){
    var cartShopBox=document.createElement("div");
    cartShopBox.classList.add("cart-box");
    var cartItem =document.getElementsByClassName('cart-content')[0];
    var cartItemName=document.querySelectorAll('.cart-product-details');
    for ( var i = 0; i <cartItemName.length; i++){
        if(id == cartItemName[i].dataset.id) {
            return
        }
    }
    var CartBoxContent=`
                <image src="${productImg}" alt="" class="cart-img"  />
                <div class="cart-details">
                    <div class="cart-product-details" data-id="${id}">${title}</div>
                    <div class="cart-price">${price}</div>
                    <input type="number" value="1" class="cart-quantity">
                </div>
                <!--remove item-->
                <i class='bx bxs-trash cart-remove'></i>

`;
    cartShopBox.innerHTML = CartBoxContent
    cartItem.appendChild(cartShopBox)
    cartShopBox.getElementsByClassName('cart-remove')[0].addEventListener('click',removeCartItem);
    cartShopBox.querySelector('.cart-quantity').addEventListener('change',quantityChanged);
    cartShopBox.getElementsByClassName('cart-remove')[0].addEventListener('click',removeCartItem);



}



function updatetotal(){
    var cartcontent=document.getElementsByClassName('cart-content')[0];
    var cartboxs=document.getElementsByClassName('cart-box');
    var total= 0 ;
    for ( var i=0; i<cartboxs.length; i++){
        var cartBox=cartboxs[i];
        var priceElemnt=cartBox.querySelector('.cart-price');
        var quantityElemnt=cartBox.querySelector('.cart-quantity');
        var price=parseFloat(priceElemnt.innerText.replace("$",""));
        var quantity=quantityElemnt.value;
        total = total +(price * quantity);
    }
    //if prise contain cents 
        total=Math.round(total * 100 /100);
        document.getElementsByClassName('total-price')[0].innerText='$'+total;
 }
