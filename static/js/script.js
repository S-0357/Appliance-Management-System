// JavaScript to switch from the welcome page to the stock management page
document.getElementById('start-btn').addEventListener('click', function() {
    document.getElementById('welcome-page').style.display = 'none';
    document.getElementById('stock-page').style.display = 'block';
});