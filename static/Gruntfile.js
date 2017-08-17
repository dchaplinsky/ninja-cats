module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        svgstore: {
            logos: {
                files: {
                    'app-assets/images/svg/svg-logo-sprite.svg': 'app-assets/images/svg/logo/*.svg'
                }
            }
        },

        watch: {
            grunt: {
                files: ['Gruntfile.js']
            },

            svgstore: {
                files: [
                    'app-assets/images/svg/logo/*.svg'
                ],
                tasks: [ 'svgstore']
            }
        }
    });

    // load npm modules
    grunt.loadNpmTasks('grunt-svgstore');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // register tasks
    grunt.registerTask('default', ['svgstore', 'watch']);
};
