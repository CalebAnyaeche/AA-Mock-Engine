var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'bESmartfisk@gmail.com',
    pass: 'BESmart2018@Fisk'
  }
});

var mailOptions = {
  from: 'bESmartfisk@gmail.com',
  to: 'basanta.dhakal@my.fisk.edu',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});