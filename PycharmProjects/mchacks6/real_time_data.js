var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://n61.meraki.com/api/v0/devices/Q2GV-XLK8-MDBK/camera/analytics/live",
  "method": "GET",
  "headers": {
    "X-Cisco-Meraki-API-Key": "c52e3bdc4349ee6eff15807deb63feaffd62c874",
    "cache-control": "no-cache",
    "Postman-Token": "88df9d22-594b-40ad-a53d-9e7449e718e0"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});