### Assignment-1: Deploying pretrained MobileNet V2 model over AWS using serverless open source framework
<ol>
<li>Pretrained MobileNet V2 model is deployed on AWS s3 bucket</li>
<li>Serverless open source framework is used to build and run application on AWS.</li>
<li>Serverless framwork manages all the resources in AWS and user need to just focus on their Application and problem solving.</li>
<li>All the AWS resources such as API end point, Lambda functions, Cloud Formations, application packages on S3 and many mores resources are created automatically.</li>
<li>It's very cool as it takes all the burden of managing AWS resources from the user.</li>
<li>Application is deploy as AWS Lambda function which fetch model from S3 bucket.</li>
</ol>
<table>
     <tr>
        <td>
          <input type="file" id="imageUpload">
          <img id="output" width="300" />
        </td>
  <td>
       <li>Due to cold start of Lambda, first time is to start the Lambda and give a second try after 90 seconds</li>
        <li id="mobilenet_imagenet">MobileNet V2 (ImageNet 1000 Classes) predicted is : </li>
    </td>
</tr>
</table>
<script>
  document.getElementById('imageUpload').onchange = function (evt) {
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
          document.getElementById("mobilenet_imagenet").innerHTML = "<p>" + "MobileNet V2 predicted for the image out of Imagenet (1000 Classes), prediction is : " + json.predicted + "</p>";
      }  
   });

};
</script>

### Assignment-2: Deploying trained MobileNet V2 model on custom flying objects data with 4 classes {flying birds, small quadcopters, large quadcopters, winged drones}
<ol>
<li>Custom trained MobileNet V2 model on flying objects is deployed on AWS s3 bucket</li>
<li>Serverless open source framework is used to build and run application on AWS.</li>
<li>Serverless framwork manages all the resources in AWS and user need to just focus on their Application and problem solving.</li>
<li>All the AWS resources such as API end point, Lambda functions, Cloud Formations, application packages on S3 and many mores resources are created automatically.</li>
<li>It's very cool as it takes all the burden of managing AWS resources from the user.</li>
<li>Application is deploy as AWS Lambda function which fetch model from S3 bucket.</li>
</ol>
<table>
     <tr>
        <td>
          <input type="file" id="imageUpload">
          <img id="output" width="300" />
        </td>
  <td>
       <li>Due to cold start of Lambda, first time is to start the Lambda and give a second try after 90 seconds</li>
        <li id="mobilenet_customdata">process started, AWS lambda retrieving model from S3 : </li>
    </td>
</tr>
</table>
<script>
  document.getElementById('imageUpload').onchange = function (evt) {
var image = document.getElementById('output');
  const files = event.target.files

  const formData = new FormData ();
  formData.append ("data", files[0]);
  console.log (formData);
 
  document.getElementById("mobilenet_customdata").innerHTML = "Fetching results....."
  fetch("https://ly1yaeusha.execute-api.ap-south-1.amazonaws.com/dev/mobilenetV2-classify-flying-objects", {
    method: "POST",
    body: formData,
  })
.then(response => response.json())
.then(json => {
 console.log (json);
      if (json.error) {
        document.getElementById("mobilenet_customdata").innerHTML = json.error;
      } else {
          document.getElementById("mobilenet_customdata").innerHTML = "<p>" + "MobileNet V2 predicted for the image out of 4 Classes, on flying objects is : " + json.classname + "</p>";
      }  
   });

};
</script>
