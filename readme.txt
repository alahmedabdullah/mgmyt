1. Clone 'mgmyt' repository:
	$git clone https://ahmabd@bitbucket.org/ahmabd/mgmyt.git

2. go to following direcory:
	$ cd ./mgmyt/backend/mgmyt/tardis/apps/

3. clone mongoquery app:
	$ git clone https://bitbucket.org/eresearchrmit/mongoquery.git ./tardis/apps/mongoquery
	
4. Install NodeJS
	$ brew install node 
	$ npm -v
	$ node -v

5. Install Webpack 
	$ sudo npm i -g webpack
	$ webpack -v

6. Install 2.13.1+ 
	$ sudo npm i -g eslint

7. Initialize your NPM package. Go to ./mgmyt/frontend/ direcoty, run
	$ npm init --yes

8. Install dev dependencies, Go to ./mgmyt/frontend/ direcoty, run
	$ npm install --save-dev eslint eslint-loader 

9. Install general dependencies, Go to ./mgmyt/frontend/ direcoty, run

	$ npm install --save webpack eslint eslint-loader angular angular-resource angular-route json-loader mustache-loader lodash

10. Please view the ./mgmyt/fronend/webpack.config.js. Please note that the webpack.config.js works for webpack version 2.2.2
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

11. execute webpack as follwowing:
	
        $ cd ./mgmyt/frontend
	$ webpack

This should produce mogoquery.js file in ./mgmyt/frontend/js directory

12. Move javascript codes to ./mgmyt/backend/mgmyt/tardis/apps/monogoquery/static directory:
        $ cd ./mgmyt/frontend
        $ ./package.sh

12. go to ./mgmyt/backend/mgmyt/tardis/apps/monogoquery
	$ cd ./mgmyt/backend/mgmyt/tardis/apps/monogoquery
	$ git add static/js/mongoquery.js
	$ git add static/mongoquery

13. commit changes to "mongoquery" repository with needed javascript files
