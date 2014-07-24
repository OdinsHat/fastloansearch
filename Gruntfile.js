module.exports = function(grunt) {
    require('time-grunt')(grunt);
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concurrent: {
            target1: ['cssmin', 'imagemin'],
            target2: ['copy', 'jshint']
        },
        jshint: {
            options: {
                reporter: require('jshint-stylish')
            },
            all: ['Gruntfile.js', 'src/js/*.js']
        },
        uglify: {
            options: {
                mangle: false,
                banner: '/* ! <%= pkg.name %>' +
                    ' <%= grunt.template.today("yyyy-mm-dd HH:MM:ss")  %> */\n'
            },
            dinobuild: {
                files: {
                    'static/js/mortgage-calculator.min.js' : ['src/js/mortgage-calculator.js'],
                    'static/js/card-calculators.min.js' : ['src/js/card-calculators.js'],
                    'static/js/search.min.js' : ['src/js/search.js'],
                }
            }
        },
        clean: {
            dinobuild: {
               src: ['static/js', 'static/css', 'static/images', 'static/*', 'static/fonts']
            }
        },
        cssmin: {
            dinobuild: {
                options: {
                    banner: '/* Minified css at <%= grunt.template.today("HH:MM:ss \'on\' yyyy-mm-dd") %> <%= pkg.version %> */'
                },
                files: {
                    'static/css/style.min.css': ['src/css/style.css', 'src/css/styles.css'],
                }
           }
        },
        imagemin: {
            norm: {
                options: {
                    optimizationLevel: 3,
                    cache: false
                },
                files: [{
                    expand: true,
                    cwd: 'src/images/',
                    src: ['**/*.{jpg,gif}'],
                    dest: 'static/images/'
                }]
            },
            hardpng: {
                options: {
                    optimizationLevel: 3,
                    cache: false,
                    pngquant: false
                },
                files: [{
                    expand: true,
                    cwd: 'src/images/',
                    src: ['**/*.png'],
                    dest: 'static/images/'
                }]
            }
        },
        copy: {
            fonts: {
                files: [
                    {
                        expand: true,
                        cwd: 'src/fonts',
                        src: ['*'],
                        dest: 'static/css/fonts/',
                        filter: 'isFile'
                    }
                ]
            },
            animatecss: {
                files: [
                    {
                        expand: true,
                        cwd: 'src/css',
                        src: ['animate.min.css'],
                        dest: 'static/css/',
                        filter: 'isFile'
                    }
                ]
            },
            /* Bootstrap is already custom built and minified by its own Gruntfile supplied by Bower */
            bootstrap: {
                files: [
                    {
                        expand: true,
                        cwd: 'src/css',
                        src: ['bootstrap-theme.min.css', 'bootstrap.min.css'],
                        dest: 'static/css/',
                        filter: 'isFile'
                    }
                ]
            }
        },
        pylint: {
            options: {
                virtualenv: '/Users/doug/.virtualenvs/fls',
                force: true
            },
            src: '*.py'
        },
        flake8: {
            options: {
                maxLineLength: 120,
                maxComplexity: 10,
                format: 'pylint',
                hangClosing: true,
                force: true
            },
            src: ['*.py']
        }
   });

    grunt.loadNpmTasks('grunt-concurrent');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-pylint');
    grunt.loadNpmTasks('grunt-flake8');

    grunt.registerTask('default', ['clean', 'copy', 'jshint', 'uglify', 'cssmin', 'imagemin']);
    grunt.registerTask('noimgs', ['copy', 'jshint', 'uglify', 'cssmin']);
    grunt.registerTask('lintpy', ['pylint', 'flake8']);
};
