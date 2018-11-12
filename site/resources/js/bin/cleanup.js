var fs = require('fs');
var path = require('path');

var current_dir = path.resolve(__dirname);
var site_dir    = path.resolve(current_dir, '../../../');
var dist_dir    = path.resolve(site_dir, 'dist/');

fs.rmdir(dist_dir, () => console.log('Done!'));
