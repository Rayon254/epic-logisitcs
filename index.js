function sendMail() {
    var params = {
      name: document.getElementById("fullname").value,
      email: document.getElementById("emailaddress").value,
      message: document.getElementById("message").value,
    };
  
    const serviceID = "service_38wxnwh";
    const templateID = "template_nxzl0lu";
  
      emailjs.send(serviceID, templateID, params)
      .then(res=>{
          document.getElementById("fullname").value = "";
          document.getElementById("emailaddress").value = "";
          document.getElementById("message").value = "";
          console.log(res);
          alert("Your message sent successfully!!")
  
      })
      .catch(err=>console.log(err));
  
  }