path = require('path')

current_dir = path.resolve(__dirname);
site_dir = path.resolve(current_dir, '../../');
assets_dir = path.resolve(site_dir, 'assets/');
build_dir = path.resolve(assets_dir, 'build/');

module.exports = {
    baseUrl: '/',
    outputDir: build_dir,
    assetsDir: '../',
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
    // delete HTML related webpack plugins
    chainWebpack: config => {
        config.plugins.delete('html')
        config.plugins.delete('preload')
        config.plugins.delete('prefetch')
    },
}