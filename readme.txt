1. Clone 'mgmyt' repository:
	$git clone https://ahmabd@bitbucket.org/ahmabd/mgmyt.git

2. Install NodeJS
	$ brew install node 
	$ npm -v
	$ node -v

3. Install Webpack 
	$ sudo npm i -g webpack
	$ webpack -v

4. Install eslint 
	$ sudo npm i -g eslint

5. Initialize your NPM package. Go to ./mgmyt/frontend/ direcoty, run
	$ npm init --yes

6. Install dev dependencies, Go to ./mgmyt/frontend/ direcoty, run
	$ npm install --save-dev eslint eslint-loader 

7. Install general dependencies, Go to ./mgmyt/frontend/ direcoty, run

	$ npm install --save webpack eslint eslint-loader angular angular-resource angular-route json-loader mustache-loader lodash

8. Please view the ./mgmyt/fronend/webpack.config.js. Please note that the webpack.config.js works for webpack version 2.2.2
        $ cd ./mgmyt/frontend
	$ webpack -verion

***However for webpack 2.3.1 following modification is needed webpack.config.js:

const path = require('path');
module.exports = {
    entry: "./app/app.js",
    output: {
        path: path.resolve(__dirname, 'dist/js'),
        filename: "bundle.js",
        sourceMapFilename: "bundle.js.map",
    },

9. execute webpack as follwowing:
	
        $ cd ./mgmyt/frontend
	$ webpack

This should produce mogoquery.js file in ./mgmyt/frontend/js directory

10. Move javascript codes to ./mgmyt/backend/mgmyt/tardis/apps/monogoquery/static directory:
        $ cd ./mgmyt/frontend
        $ ./package.sh

11. go to ./mgmyt/backend/mgmyt/tardis/apps/monogoquery
	$ cd ./mgmyt/backend/mgmyt/tardis/apps/monogoquery
	$ git add static/js/mongoquery.js
	$ git add static/mongoquery

12. commit changes to "mongoquery" repository with needed javascript files
