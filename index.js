const jsonfile = require('jsonfile');
const FILE_PATH = './XSS_check.py';
const moment = require('moment');
const simpleGit = require('simple-git');

const getRandomInt = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};

const makeCommit = n => {
    if (n === 0) {
        simpleGit().push(['origin', 'main']); // Specify the remote and branch to push to
        return;
    }

    const x = getRandomInt(0, 54);
    const y = getRandomInt(0, 6);
    const DATE = moment()
        .subtract(2, 'y')
        .add(4, 'd')
        .add(x, 'w')
        .add(y, 'd')
        .format();

    const data = {
        date: DATE
    };
    console.log(DATE);

    jsonfile.writeFile(FILE_PATH, data, (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return;
        }

        simpleGit()
            .add([FILE_PATH])
            .commit(DATE, { '--date': DATE }, makeCommit.bind(this, --n));
    });
}

makeCommit(108);