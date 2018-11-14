const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */


/*
 * Override webpack.config.js, without editing the file directly.
 */
mix.webpackConfig({
    resolve: {
        alias: {
            'site_helpers': path.resolve(__dirname, 'resources/js/site_helpers.js'),
        },
    },
});

/*
 *  Will be passed to Webpack's Provider Plugin.
 */
mix.autoload({
    //jquery: ['$', 'jQuery', 'window.jQuery']
});

/*
 *  mix.options({
 *      extractVueStyles: false, // Extract .vue component styling to file, rather than inline.
 *      globalVueStyles: file, // Variables file to be imported in every component.
 *      processCssUrls: true, // Process/optimize relative stylesheet url()'s. Set to false, if you don't want them touched.
 *      purifyCss: false, // Remove unused CSS selectors.
 *      uglify: {}, // Uglify-specific options. https://webpack.github.io/docs/list-of-plugins.html#uglifyjsplugin
 *      postCss: [] // Post-CSS options: https://github.com/postcss/postcss/blob/master/docs/plugins.md
 *  });
 */
mix.options({
    processCssUrls: false
});

/*
 |--------------------------------------------------------------------------
 | Do the Mixing!!
 |--------------------------------------------------------------------------
 */

mix.setPublicPath('.')

mix.sass('resources/sass/app.scss', 'assets/css/');

mix.js('resources/js/app.js', 'assets/js/');

//mix.copy('node_modules/@fortawesome/fontawesome-free/webfonts/', 'public/assets/fonts/');

/*
|--------------------------------------------------------------------------
| Versioning for the entire project
|--------------------------------------------------------------------------
*/

//mix.version();
