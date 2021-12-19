  function calculateSentiment() {
    url = document.getElementById("input_url");
    check_sentiment_url = '{% url "main:home" %}';
    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', '{{ csrf_token }}')
    formData.append('input_url', url)

    $.ajax({
        type: 'POST',
        url: check_sentiment_url,
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        enctype: 'multipart/form-data',
        success: function (response) {
            data = JSON.parse(JSON.stringify(response));
            alert(`Result: ${data.pos}`);
            //location.reload();
        },
        error: function (xhr, errmsg, err) {
            console.log(`ERROR: ${err}. Message: ${errmsg}. XHR: ${xhr}`)
            alert(`Failed calculation`)
        }
    })                
}
