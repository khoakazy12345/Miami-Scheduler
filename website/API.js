const express = require('express');
const site = express();
const mongoose = require('mongoose');
const path = require('path');
const cors = require('cors');

site.use(cors());
site.use(express.static(__dirname + "/index"));


mongoose.connect('mongodb://localhost/MiamiCourses')
    .then(() => console.log('Getting connected to MongoDB'))
    .catch(err => console.log('Error happened'));

const Schema = mongoose.Schema;
const preReqCourses = new Schema({
    courseName: String,
    Prereqs:[String],
    CoReqs: [String]
});

const Course = mongoose.model('course',preReqCourses);


site.get('/courses/:course',async (req,res) =>{
    let course = req.params.course;
    let arrayPre = await getCourseWithPre(course);
    res.send(arrayPre);
});

async function getCourseWithPre(course){
    const coursesPreReqs = await Course.find({Prereqs: course});
    console.log(coursesPreReqs);
    return coursesPreReqs;
}

site.post('/courses/:course',(req,res) =>{
    let course = res.params.course;
    let courseNum = res.params.courseNum;

    console.log(`${course} & ${courseNum} were posted`);
});

site.delete('/courses/:course',(req,res) => {
    let course = res.params.course;
    let courseNum = res.params.courseNum;

    console.log(`${course} & ${courseNum}`);
});

site.listen(8080,() => console.log("Listening on port 8080"));