const spawn = require("child_process").spawn;

const pythonProcess = spawn('python',[getcommentscopy.py]);
pythonProcess.stdout.on('data',(data) => {
    mystr = data.toString();
    myjson = JSON.parse(mystr);
    console.log(myjson);
});

