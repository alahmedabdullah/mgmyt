module.exports = {  
    entry: "./mongoquery/app.js",
    output: {
        path: "./js/",
        filename: "mongoquery.js",
        sourceMapFilename: "mongoquery.js.map",
    },


    module: {
        rules: [{
            test: /\.js$/,
            enforce: "pre",
            exclude: /node-modules/,
            }],
        rules: [{
            test: /\.js$/,
            enforce: "pre",
            loader: "eslint-loader",
            }],
        rules: [{
            test: /\.js$/,
            use: [
              {
                  loader: "style-loader"
              },
              {
                  loader: "css-loader",
                  options: {
                      modules: true
                  }
              }]
              }],
        rules: [{
            test: /\.html$/,
            use: [
              {
                  loader: "mustache-loader"
              }]
            }]
    },
    resolve: {
           enforceExtension: false
    }

};
