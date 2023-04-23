var xhr = new XMLHttpRequest();
xhr.open('GET', 'json/ram.json');
xhr.onload = function() {
  if (xhr.status === 200) {
    var data = JSON.parse(xhr.responseText);
    var dropdown = document.getElementById('gameram');
    for (var i = 0; i < data.options.length; i++) {
      var option = document.createElement('option');
      option.text = data.options[i];
      dropdown.add(option);
    }
  }
};
xhr.send();