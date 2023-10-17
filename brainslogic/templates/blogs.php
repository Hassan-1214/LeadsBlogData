<!doctype html>
<html lang="en">

<?php
include_once 'head.php'
?>
<script>

function get_blogs(){

    console.log('Entered')
    
    $.ajax({
        type: "GET",
    url: 'http://127.0.0.1:8000/blog/',
    // data: JSON.stringify({ qa: 'test' }),
    headers: {
        "Content-Type": "application/json",
        // "Authorization": "Bearer " +  jwt
    },
    success: function (data) {
        // var jwt = window.localStorage.getItem('jwt')
        console.log(data);
    },
    error: function (request, status, error) {
        showToast("Something went wrong! please try again later.")
    }
});

}


// $.ajax({
//     type: "POST",
//     url: api_url + "/customer/submit-customer-qa/",
//     data: JSON.stringify({ qa: qaPayload }),
//     headers: {
//     "Content-Type": "application/json",
//     "Authorization": "Bearer " +  jwt
//     },
//     success: function (data) {
//         closePopup()
//         location.reload();
//     },
//     error: function (request, status, error) {
//         showToast("Something went wrong! please try again later.")
//     }
// });










    </script>
<body class="home-dark2 tt-magic-cursor" onload="get_blogs()">
<?php
$a = $b = $c = $d = $e = $f = $g = 'none';
$d = 'active';
include_once 'nav.php'
?>
<!-- Start breadcrumbs section -->
<section class="breadcrumbs">
    <div class="breadcrumb-sm-images">
        <div class="inner-banner-1 magnetic-item">
            <img src="assets/img/inner-pages/inner-banner-1.png" alt="">
        </div>
        <div class="inner-banner-2 magnetic-item">
            <img src="assets/img/inner-pages/inner-banner-2.png" alt="">
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <div class="breadcrumb-wrapper">
                    <div class="breadcrumb-cnt">
                        <span>Blogs</span>
                        <h1>"Exploring The BrainsLogic Blog"</h1>
                        <div class="breadcrumb-list">
                            <a href="https://www.brainslogic.com">Home</a><img src="assets/img/inner-pages/breadcrumb-arrow.svg" alt="">
                            Blogs
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- End breadcrumbs section -->
<div class="blog-banner sec-mar">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="blog-banner-wrap">
                    <div class="banner-img">
                        <img src="assets/img/inner-pages/blog-banner.png" alt="">
                    </div>
                    <div class="banner-content">
                        <h2>Blog</h2>
                        <p>Join 50,000+ Subscribers</p>
                        <form>
                            <div class="form-inner">
                                <input type="text" placeholder="Email here...">
                                <button type="submit">
                                    Subscribe
                                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 1H12M12 1V13M12 1L0.5 12"></path>
                                    </svg>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="home3-blog-area sec-mar">
    <div class="container">
        <div class="row g-lg-4 gy-5">
            <div class="col-lg-4 col-md-6 wow animate fadeInLeft" data-wow-delay="300ms" data-wow-duration="1500ms">
                <div class="single-blog magnetic-item">
                    <div class="blog-img">
                        <img class="img-fluid" src="assets/img/home-3/home3-blog-01.png" alt="">
                        <div class="blog-tag">
                            <a href="blogs.php">Web development</a>
                        </div>
                    </div>
                    <div class="blog-content">
                        <ul class="blog-meta">
                            <li><a href="blogs.php">May 20, 2023</a></li>
                            <li><a href="blogs.php">Comment (3)</a></li>
                        </ul>
                        <h4><a href="blog-details.php">Donec finibus laoreet exte eu pellentesque. </a></h4>
                        <div class="blog-footer">
                            <div class="read-btn">
                                <a href="blog-details.php">Read More
                                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 1H12M12 1V13M12 1L0.5 12"></path>
                                    </svg>
                                </a>
                            </div>
                            <div class="social-area">
                                <ul>
                                    <li><a href="https://www.facebook.com/"><i class="bx bxl-facebook"></i></a></li>
                                    <li><a href="https://twitter.com/"><i class="bx bxl-twitter"></i></a></li>
                                    <li><a href="https://www.pinterest.com/"><i class="bx bxl-pinterest-alt"></i></a>
                                    </li>
                                    <li><a href="https://www.instagram.com/"><i class="bx bxl-instagram"></i></a></li>
                                </ul>
                                <span><img src="assets/img/home-3/plain-icon.svg" alt=""></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 wow animate fadeInUp" data-wow-delay="200ms" data-wow-duration="1500ms">
                <div class="single-blog magnetic-item">
                    <div class="blog-img">
                        <img class="img-fluid" src="assets/img/home-3/home3-blog-02.png" alt="">
                        <div class="blog-tag">
                            <a href="blogs.php">Cloud solutions</a>
                        </div>
                    </div>
                    <div class="blog-content">
                        <ul class="blog-meta">
                            <li><a href="blogs.php">May 20, 2023</a></li>
                            <li><a href="blogs.php">Comment (3)</a></li>
                        </ul>
                        <h4><a href="blog-details.php">feugiat varius mattis mass enim est egestas.</a></h4>
                        <div class="blog-footer">
                            <div class="read-btn">
                                <a href="blog-details.php">Read More
                                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 1H12M12 1V13M12 1L0.5 12"></path>
                                    </svg>
                                </a>
                            </div>
                            <div class="social-area">
                                <ul>
                                    <li><a href="https://www.facebook.com/"><i class="bx bxl-facebook"></i></a></li>
                                    <li><a href="https://twitter.com/"><i class="bx bxl-twitter"></i></a></li>
                                    <li><a href="https://www.pinterest.com/"><i class="bx bxl-pinterest-alt"></i></a>
                                    </li>
                                    <li><a href="https://www.instagram.com/"><i class="bx bxl-instagram"></i></a></li>
                                </ul>
                                <span><img src="assets/img/home-3/plain-icon.svg" alt=""></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 wow animate fadeInRight" data-wow-delay="300ms" data-wow-duration="1500ms">
                <div class="single-blog magnetic-item">
                    <div class="blog-img">
                        <img class="img-fluid" src="assets/img/home-3/home3-blog-03.png" alt="">
                        <div class="blog-tag">
                            <a href="blogs.php">Web development</a>
                        </div>
                    </div>
                    <div class="blog-content">
                        <ul class="blog-meta">
                            <li><a href="blogs.php">May 20, 2023</a></li>
                            <li><a href="blogs.php">Comment (3)</a></li>
                        </ul>
                        <h4><a href="blog-details.php">Navigating the Journey off Cloud Solution.</a></h4>
                        <div class="blog-footer">
                            <div class="read-btn">
                                <a href="blog-details.php">Read More
                                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 1H12M12 1V13M12 1L0.5 12"></path>
                                    </svg>
                                </a>
                            </div>
                            <div class="social-area">
                                <ul>
                                    <li><a href="https://www.facebook.com/"><i class="bx bxl-facebook"></i></a></li>
                                    <li><a href="https://twitter.com/"><i class="bx bxl-twitter"></i></a></li>
                                    <li><a href="https://www.pinterest.com/"><i class="bx bxl-pinterest-alt"></i></a>
                                    </li>
                                    <li><a href="https://www.instagram.com/"><i class="bx bxl-instagram"></i></a></li>
                                </ul>
                                <span><img src="assets/img/home-3/plain-icon.svg" alt=""></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 wow animate fadeInLeft" data-wow-delay="300ms" data-wow-duration="1500ms">
                <div class="single-blog magnetic-item">
                    <div class="blog-img">
                        <img class="img-fluid" src="assets/img/home-3/home3-blog-04.png" alt="">
                        <div class="blog-tag">
                            <a href="blogs.php">Web development</a>
                        </div>
                    </div>
                    <div class="blog-content">
                        <ul class="blog-meta">
                            <li><a href="blogs.php">May 20, 2023</a></li>
                            <li><a href="blogs.php">Comment (3)</a></li>
                        </ul>
                        <h4><a href="blog-details.php">Donec finibus laoreet exte eu pellentesque. </a></h4>
                        <div class="blog-footer">
                            <div class="read-btn">
                                <a href="blog-details.php">Read More
                                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 1H12M12 1V13M12 1L0.5 12"></path>
                                    </svg>
                                </a>
                            </div>
                            <div class="social-area">
                                <ul>
                                    <li><a href="https://www.facebook.com/"><i class="bx bxl-facebook"></i></a></li>
                                    <li><a href="https://twitter.com/"><i class="bx bxl-twitter"></i></a></li>
                                    <li><a href="https://www.pinterest.com/"><i class="bx bxl-pinterest-alt"></i></a>
                                    </li>
                                    <li><a href="https://www.instagram.com/"><i class="bx bxl-instagram"></i></a></li>
                                </ul>
                                <span><img src="assets/img/home-3/plain-icon.svg" alt=""></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 wow animate fadeInUp" data-wow-delay="200ms" data-wow-duration="1500ms">
                <div class="single-blog magnetic-item">
                    <div class="blog-img">
                        <img class="img-fluid" src="assets/img/home-3/home3-blog-05.png" alt="">
                        <div class="blog-tag">
                            <a href="blogs.php">Cloud solutions</a>
                        </div>
                    </div>
                    <div class="blog-content">
                        <ul class="blog-meta">
                            <li><a href="blogs.php">May 20, 2023</a></li>
                            <li><a href="blogs.php">Comment (3)</a></li>
                        </ul>
                        <h4><a href="blog-details.php">feugiat varius mattis mass enim est egestas.</a></h4>
                        <div class="blog-footer">
                            <div class="read-btn">
                                <a href="blog-details.php">Read More
                                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 1H12M12 1V13M12 1L0.5 12"></path>
                                    </svg>
                                </a>
                            </div>
                            <div class="social-area">
                                <ul>
                                    <li><a href="https://www.facebook.com/"><i class="bx bxl-facebook"></i></a></li>
                                    <li><a href="https://twitter.com/"><i class="bx bxl-twitter"></i></a></li>
                                    <li><a href="https://www.pinterest.com/"><i class="bx bxl-pinterest-alt"></i></a>
                                    </li>
                                    <li><a href="https://www.instagram.com/"><i class="bx bxl-instagram"></i></a></li>
                                </ul>
                                <span><img src="assets/img/home-3/plain-icon.svg" alt=""></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 wow animate fadeInRight" data-wow-delay="300ms" data-wow-duration="1500ms">
                <div class="single-blog magnetic-item">
                    <div class="blog-img">
                        <img class="img-fluid" src="assets/img/home-3/home3-blog-06.png" alt="">
                        <div class="blog-tag">
                            <a href="blogs.php">Web development</a>
                        </div>
                    </div>
                    <div class="blog-content">
                        <ul class="blog-meta">
                            <li><a href="blogs.php">May 20, 2023</a></li>
                            <li><a href="blogs.php">Comment (3)</a></li>
                        </ul>
                        <h4><a href="blog-details.php">Navigating the Journey off Cloud Solution.</a></h4>
                        <div class="blog-footer">
                            <div class="read-btn">
                                <a href="blog-details.php">Read More
                                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 1H12M12 1V13M12 1L0.5 12"></path>
                                    </svg>
                                </a>
                            </div>
                            <div class="social-area">
                                <ul>
                                    <li><a href="https://www.facebook.com/"><i class="bx bxl-facebook"></i></a></li>
                                    <li><a href="https://twitter.com/"><i class="bx bxl-twitter"></i></a></li>
                                    <li><a href="https://www.pinterest.com/"><i class="bx bxl-pinterest-alt"></i></a>
                                    </li>
                                    <li><a href="https://www.instagram.com/"><i class="bx bxl-instagram"></i></a></li>
                                </ul>
                                <span><img src="assets/img/home-3/plain-icon.svg" alt=""></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <nav aria-label="Page navigation example">
                <ul class="pagination justify-content-center">
                    <li class="page-item disabled">
                        <a class="page-link"><i class="bi bi-arrow-left"></i></a>
                    </li>
                    <li class="page-item"><a class="page-link active" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                        <a class="page-link" href="#"><i class="bi bi-arrow-right"></i></a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</div>
<!-- Start Footer section -->
<?php
include_once 'footer.php';
?>
<!-- End Footer section -->



</body>

</html>