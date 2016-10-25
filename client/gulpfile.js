var gulp   = require('gulp');
var sass   = require('gulp-sass');
var concat = require('gulp-concat');
var watch  = require('gulp-watch');

gulp.task('css', function () {
     var css = [
        'node_modules/angular-material/angular-material.min.css',
    ];

    gulp.src(css)
        .pipe(concat('styles.css'))
        .pipe(gulp.dest('../static/css'));
})

gulp.task('scripts', function(){
    var scripts = [
        // Dist
        'node_modules/angular/angular.min.js',
        'node_modules/angular-animate/angular-animate.min.js',
        'node_modules/angular-aria/angular-aria.min.js',
        'node_modules/angular-messages/angular-messages.min.js',
        'node_modules/angular-mocks/angular-mocks.js',
        'node_modules/angular-sanitize/angular-sanitize.min.js',
        'node_modules/angular-material/angular-material.min.js',
        'src/app.js'
    ];

    gulp.src(scripts)
        .pipe(concat('script.js'))
        .pipe(gulp.dest('../static/js'));
});

gulp.task('watch', function() {
    gulp.start('scripts')
    gulp.start('css')
    gulp.watch('src/**/*', ['scripts']);
});

gulp.task('default', [
    'scripts', 'css'
]);
