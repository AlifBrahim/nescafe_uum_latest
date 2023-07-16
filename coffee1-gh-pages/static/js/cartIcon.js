document.addEventListener("DOMContentLoaded", function() {
    const cartIcon = document.querySelector('.cart .bag small');
    let cartCount = 0;

    // Retrieve cartCount from localStorage on page load
    window.addEventListener('load', () => {
        cartCount = parseInt(localStorage.getItem('cartCount')) || 0;
        cartIcon.textContent = cartCount;
    });
    console.log('cartCount: ', cartCount);
    console.log('parseInt(localStorage.getItem(\'cartCount\')): ', parseInt(localStorage.getItem('cartCount')))
});
