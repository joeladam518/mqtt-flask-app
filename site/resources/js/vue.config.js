var path = require('path');

var current_dir = path.resolve(__dirname);
var site_dir    = path.resolve(current_dir, '../../');
var assets_dir  = path.resolve(site_dir, 'assets/');
var js_dir   = path.resolve(assets_dir, 'js/');

module.exports = {
    baseUrl: '/',
    outputDir: js_dir,
    assetsDir: '../',
    filenameHashing: false,
    lintOnSave: false,
    css: {
        extract: true,
        sourceMap: true,
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
        config.optimization.delete('splitChunks')
        // Set aliases
        config.resolve.alias.set("@public_assets", assets_dir);
    },
};
