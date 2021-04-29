$("#login-form").submit(function(event) {
    event.preventDefault();
    const formData = $(this).serializeArray();

    const dataObj = formData.reduce((acc, data) => {
        acc[data.name] = data.value;
        return acc;
    }, {});

    console.log(dataObj);

    $.ajax({
        url: "/admin/login",
        type: "post",
        data: JSON.stringify(dataObj),
        contentType: "application/json; charset=utf-8",
        success: function() {
            console.log("Successful login");
            window.location.href = "/admin";
        },
        error: function() {
            alert("Unsuccessful login");
        }
    })
});

$("#logout-cta").click(function(event) {
    event.preventDefault();

    $.ajax({
        url: "/seller/logout",
        type: "delete",
        contentType: "application/json; charset=utf-8",
        success: function() {
            console.log("Successful logout");
            window.location.href = "/admin/login";
        },
        error: function() {
            alert("Unsuccessful logout");
        }
    })
});


$("#login-form-buyer").submit(function(event) {
    event.preventDefault();
    const formData = $(this).serializeArray();

    const dataObj = formData.reduce((acc, data) => {
        acc[data.name] = data.value;
        return acc;
    }, {});

    console.log(dataObj);

    $.ajax({
        url: "/customer/login",
        type: "post",
        data: JSON.stringify(dataObj),
        contentType: "application/json; charset=utf-8",
        success: function() {
            console.log("Successful login");
            window.location.href = "/";
        },
        error: function() {
            alert("Unsuccessful login");
        }
    })
});

$("#logout-cta-buyer").click(function(event) {
    event.preventDefault();

    $.ajax({
        url: "/customer/logout",
        type: "delete",
        contentType: "application/json; charset=utf-8",
        success: function() {
            console.log("Successful logout");
            window.location.href = "/customer/login";
        },
        error: function() {
            alert("Unsuccessful logout");
        }
    })
});
