(function () {
    var MAX_DURATION = 60;

    function checkDuration(input) {
        var file = input.files && input.files[0];
        if (!file) return;

        var video = document.createElement('video');
        video.preload = 'metadata';
        video.onloadedmetadata = function () {
            window.URL.revokeObjectURL(video.src);
            if (video.duration > MAX_DURATION) {
                alert('La vidéo dure ' + Math.round(video.duration) + 's. Maximum autorisé : ' + MAX_DURATION + 's.');
                input.value = '';
            }
        };
        video.src = window.URL.createObjectURL(file);
    }

    document.addEventListener('DOMContentLoaded', function () {
        var input = document.getElementById('id_video');
        if (input) {
            input.addEventListener('change', function () {
                checkDuration(input);
            });
        }
    });
})();
