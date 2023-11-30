let images = [
    "./images/CD54B0A4-BE03-437D-8D68-C3BCB6C43748.JPG",
    "./images/IMG_2368.jpg", 
    "./images/IMG_8068.jpg"
    ];
    let currentImage = 0;
    
    function changeBackgroundImage() {
        document.body.style.backgroundImage = `url(${images[currentImage]})`;
        currentImage = (currentImage + 1) % images.length;
    }
    
    setInterval(changeBackgroundImage, 5000); // Change every 5 seconds