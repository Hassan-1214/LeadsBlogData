<?php
// Define the error page URL
$errorPage = "error.php";

// Get the requested URL
$requestUrl = $_SERVER['REQUEST_URI'];

// Remove query parameters from the URL if needed
$requestUrl = strtok($requestUrl, '?');

// Check if the requested file or page exists
if (!file_exists($_SERVER['DOCUMENT_ROOT'] . $requestUrl)) {
    // Set the HTTP response status code to 404 (Not Found)
    header("HTTP/1.0 404 Not Found");

    // Redirect to the error page
    header("Location: $errorPage");
    exit; // Ensure that the script stops executing after the redirect
}

// If the URL is valid and the file/page exists, continue with your regular script logic here
?>


<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description"
          content="Welcome to BrainsLogic, where innovation meets excellence! We offer Web Design, Web Development, Mobile App Development Digital Marketing, Data Scraping, and Automation services. Let us transform your ideas into captivating realities for digital success.">
    <meta name="keywords"
          content="web design, software house in pakistan, website developer in pakistan, best web design agency, web design agency, web development, digital marketing, data scraping,  web automation, software house, custom web development, responsive web design, websites, responsive, HTML, CSS, bootstrap, Django, Python, PHP, CMS, CRM, ERP, SAAS, bootstrap5, figma to HTML, figma to website, figma to Bootstrap, web development agency">


    <!-- Bootstrap CSS -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icon CSS -->
    <link href="assets/css/bootstrap-icons.css" rel="stylesheet">
    <!-- Fontawesome all CSS -->
    <link href="assets/css/all.min.css" rel="stylesheet">

    <!-- Google Captcha   -->
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

    <!-- Fontawesome CSS -->
    <link href="assets/css/fontawesome.min.css" rel="stylesheet">
    <!-- Swiper slider CSS -->
    <link rel="stylesheet" href="assets/css/swiper-bundle.min.css">

    <!-- Animate CSS -->
    <link rel="stylesheet" href="assets/css/animate.min.css">
    <link rel="stylesheet" href="assets/css/jquery.fancybox.min.css">
    <!-- BoxIcon  CSS -->
    <link href="assets/css/boxicons.min.css" rel="stylesheet">
    <!--  Style CSS  -->
    <link rel="stylesheet" href="assets/css/preloader.css">
    <link rel="stylesheet" href="assets/css/style2.css">
    <!-- Title -->
    <title>BrainsLogic - Software Agency and creative IT solution</title>
    <link rel="icon" href="assets/img/pre-loader.png" type="image/gif" sizes="20x20">
    <link rel="apple-touch-icon" sizes="76x76" href="assets/img/pre-loader.png">
</head>

