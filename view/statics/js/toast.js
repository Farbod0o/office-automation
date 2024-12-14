// toast.js

function showToast(type, message) {
    const toastContainer = document.getElementById('toast-container');


    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;


    const closeButton = document.createElement('button');
    closeButton.className = 'close-btn';
    closeButton.innerHTML = '&times;';
    closeButton.onclick = () => {
        toast.classList.remove('show');
        setTimeout(() => toastContainer.removeChild(toast), 300);
    };

    toast.appendChild(closeButton);
    toastContainer.appendChild(toast);


    setTimeout(() => toast.classList.add('show'), 100);


    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toastContainer.contains(toast) && toastContainer.removeChild(toast), 300);
    }, 3000);
}
