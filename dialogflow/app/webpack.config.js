
const path = require('path');
const nodeExternals = require('webpack-node-externals');
const slsw = require('serverless-webpack');
const webpack = require('webpack');

module.exports = {
    entry: slsw.lib.entries,
    target: 'node',
    mode: 'development',
    externals: [nodeExternals],
    resolve: {
        extensions: [
          '.js',
          '.jsx',
          '.json',
          '.ts',
          '.tsx'
        ]
    },
    output: {
        libraryTarget: 'commonjs',
        path: path.join(__dirname, '.webpack'),
        filename: '[name].js'
    },
    module: {
        rules: [
          { test:  /\.ts(x?)$/, loader: 'ts-loader' }
        ]
    },
    externals: ["aws-sdk"],
    optimization: {
      minimize: false
    },
    plugins: [
        new webpack.IgnorePlugin(/^pg-native$/)
      ]
}