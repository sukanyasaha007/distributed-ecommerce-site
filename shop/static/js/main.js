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
        },
        error: function() {
            console.log("Unsuccessful login");
        }
    })
});

