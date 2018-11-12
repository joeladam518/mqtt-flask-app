var path = require('path');

var current_dir = path.resolve(__dirname);
var site_dir    = path.resolve(current_dir, '../../');
var dist_dir   = path.resolve(site_dir, 'dist/');
var assets_dir  = path.resolve(site_dir, 'assets/');

module.exports = {
    baseUrl: '/',
    outputDir: dist_dir,
    assetsDir: '../assets/',
    filenameHashing: false,
    lintOnSave: false,
    css: {
        extract: true,
        loaderOptions: {
            css: {
                // options here will be passed to css-loader
            },
            postcss: {
                // options here will be passed to postcss-loader
            },
        },
    },
    pluginOptions: {
        // plugins can access these options as
        // `options.pluginOptions.foo`.
    },
    chainWebpack: config => {
        // delete HTML related webpack plugins
        config.plugins.delete('html')
        config.plugins.delete('preload')
        config.plugins.delete('prefetch')
        // Set aliases
        config.resolve.alias.set("@public_assets", assets_dir);
    },
};
