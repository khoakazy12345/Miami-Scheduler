const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/MiamiCourses');
const Schema = mongoose.Schema;
const preReqCourses = new Schema({
    courseName: String,
    Prereqs:[String]
});
const Course = mongoose.model('Course',preReqCourses);

async function createCourse(courseName,preReqs){
    course = new Course({
        courseName: courseName,
        Prereqs: preReqs
    });

    courseSave = await course.save();
    console.log(`${courseSave}`);
}

