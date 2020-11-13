const express = require('express');
const app = express();
const studentRoute = express.Router();
let multer = require('multer');

let alert = require('alert');

var async = require('async');

const path = require('path');
const {spawn} = require('child_process');
var fs = require('fs');
var process = require('process');

const DIR = './requirements/';

// Student model
let Student = require('../model/Student');
let reqfile;
studentRoute.post('/test-req', (req, res, next) => {

      res.json(data)

      const {PythonShell} = require("python-shell");
      var pyshell = new PythonShell('req_test.py');

      pyshell.send(JSON.stringify([req.body.candidate_name, req.body.candidate_email]));

      pyshell.on('message', function (message) {
          // received a message sent from the Python script (a simple "print" statement)
          console.log(message);
        
          alert(message); 
      });

      // end the input stream and allow the process to exit
      pyshell.end(function (err) {
          if (err){
              throw err;
          };

          console.log('finished');
      });


});
  studentRoute.post('/check-id', (req, res, next) => {

        // console.log(req.body.candidate_email)
        // alert("checking id")
        const {PythonShell} = require("python-shell");
        var pyshell = new PythonShell('generate_id.py');
    
        pyshell.send(JSON.stringify(req.body.candidate_email));
    
        pyshell.on('message', function (message) {
            // received a message sent from the Python script (a simple "print" statement)
            console.log(message);
            alert(message)
        });
    
        // end the input stream and allow the process to exit
        pyshell.end(function (err) {
            if (err){
                throw err;
            };
    
            console.log('finished');
        });
      
        });
  
  studentRoute.post('/train-model', (req, res, next) => {
  
   
          fs.writeFile('filename.txt',req.body.candidate_name, function(err){
            if (err) return console.log(err);

          } );
          fs.writeFile('projectname.txt',req.body.section, function(err){
            if (err) return console.log(err);

          } );
          // res.json(data)
          alert("Training a model, Please wait!")
          const {PythonShell} = require("python-shell");
          var pyshell = new PythonShell('preprocess_train.py');
      
          pyshell.send(JSON.stringify([req.body.candidate_name,req.body.section]));
      
          pyshell.on('message', function (message) {
              // received a message sent from the Python script (a simple "print" statement)
              console.log(message);
          });
      
          // end the input stream and allow the process to exit
          pyshell.end(function (err) {
              if (err){
                  throw err;
              };
      
              console.log('finished');
              alert("Model file created")
          });
    
});

// Add Student

studentRoute.route('/add-student').post((req, res, next) => {
 
      // alert("Retrieving Requirements, Please wait")
      const {PythonShell} = require("python-shell");
      var pyshell = new PythonShell('get_data3.py');

      pyshell.send(JSON.stringify([req.body.candidate_name, req.body.candidate_email]));

      pyshell.on('message', function (message) {
          // received a message sent from the Python script (a simple "print" statement)
          console.log(message);
      
        
      });

    // end the input stream and allow the process to exit
      pyshell.end(function (err) {
          if (err){
              throw err;
          };

          console.log('finished');
      });
      // process.exit();

});

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, DIR);
  },
  filename: (req, file, cb) => {
    const fileName = file.originalname.toLowerCase().split(' ').join('-');
    cb(null, fileName)
  }
});

var upload = multer({
  storage: storage,
  // limits: {
  //   fileSize: 1024 * 1024 * 5
  // },
  fileFilter: (req, file, cb) => {
    if (true) {
      cb(null, true);
    } else {
      cb(null, false);
      return cb(new Error('Only CSV, XLS or XLSX format allowed!'));
    }
  }
});

// User model
// let User = require('../models/User');

studentRoute.post('/create-user', upload.array('avatar', 20), (req, res, next) => {
  const reqFiles = []
  const url = req.protocol + '://' + req.get('host')
  for (var i = 0; i < req.files.length; i++) {
    reqFiles.push(url + '/requirements/' + req.files[i].filename)
    console.log("uploaded successfully!")
    
  }
  
  // let options = {
  //   args: ['requirements/' + req.files[0].filename]
  // };
  //  console.log(options)
  // PythonShell.run('req_trace.py', options, function (err, results) {
  //   if (err) throw err;
  //   // results is an array consisting of messages collected during execution
  //   console.log('results: %j', results);
  // });

});

// Get all student
studentRoute.route('/').get((req, res) => {
  Student.find((error, data) => {
    if (error) {
      return next(error)
    } else {
      res.json(data)
      
    }
  })
  
})

module.exports = studentRoute;