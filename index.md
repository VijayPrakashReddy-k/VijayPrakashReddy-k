
<table>
     <tr>
        <td>
          <input type="file" id="imageUpload">
          <img id="output" width="300" />
        </td>
  <td>
       <li>Due to cold start of Lambda, first time is to start the Lambda and give a second try after 90 seconds</li>
        <li id="mobilenet_imagenet">MobileNet V2 (ImageNet 1000 Classes)</li>
    </td>
</tr>
</table>
<script>
  document.getElementById('imageUpload').onchange = function (evt) {
alert("Image");
var image = document.getElementById('output');
  const files = event.target.files

  const formData = new FormData ();
  formData.append ("data", files[0]);
  console.log (formData);
 
  document.getElementById("mobilenet_imagenet").innerHTML = "Fetching results....."
  fetch("https://tda3oz8ho9.execute-api.ap-south-1.amazonaws.com/dev/mobilenetV2-classify", {
    method: "POST",
    body: formData,
  })
.then(response => response.json())
.then(json => {
 console.log (json);
      if (json.error) {
        document.getElementById("mobilenet_imagenet").innerHTML = json.error;
      } else {
        document.getElementById("mobilenet_imagenet").innerHTML = json.predicted[1];
      }  
   });

};
</script>
