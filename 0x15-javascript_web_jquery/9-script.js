$('document').ready(function () {
    $.get("https://stefanbohacek.com/hellosalut/?lang=fr", function (response) {
      $('div#hello').html(response.hello);
    });
  });