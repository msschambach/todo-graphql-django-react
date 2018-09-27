const webpack = require('webpack');
const path = require('path');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

const WebpackConfig = {
    entry: {
        'todo': './applications/todo/js/todoapp/index.js'
    },

    output: {
        path: path.resolve('./applications/todo/dist'),
        filename: '[name].bundle.js'
    },

    module: {
        rules: [
            {
                test: /\.m?js$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['es2015', 'react']
                    }
                },
                exclude: /(node_modules|bower_components)/
            },
            {
                test: /\.jsx$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['es2015', 'react']
                    }
                },
                exclude: /(node_modules|bower_components)/
            },
            {
                test: /\.css$/,
                loader: 'css-loader'
            },
            {
                test: /\.(gif|png|jpe?g|svg)$/i,
                use: [
                    'file-loader'
                ],
                exclude: /(node_modules|bower_components)/
            }
        ]
    },

    plugins: [
        new webpack.DefinePlugin({
            'process.env': { NODE_ENV: JSON.stringify(process.env.NODE_ENV || '"development"') }
        }),
        new UglifyJsPlugin({
            sourceMap: true,
            uglifyOptions: {
                ie8: true,
                compress: true,
                output: {
                    comments: false,
                    beautify: false
                }
            }
        })
    ],

    target: 'node',

    mode: 'development',

    devtool: 'source-map'
};

module.exports = WebpackConfig;