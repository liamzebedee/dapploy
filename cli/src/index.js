'use strict';

const program = require('commander');

require('pretty-error').start();
require('dotenv').config();

require('./commands/publish').cmd(program);

program.parse(process.argv);
