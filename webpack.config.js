// webpack.config.js
const path = require('path');

const basePath = './src/redturtle/reactbundle/browser/static';

module.exports = {
  entry: {
    react: path.resolve(__dirname, basePath, 'react-vendor.js'),
  },

  output: {
    path: path.resolve(__dirname, basePath, 'dist'),
    filename: '[name].min.js',
  },

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
    ],
  },
  devtool: 'source-map',
};
