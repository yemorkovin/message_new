 $('.show_errors').hide();
 $('#reg_btn').on('click', function(){
    let email = $('#email').val();
    let password = $('#password').val();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url: '/ajaxReg',
        method: 'post',
        dataType: 'html',
        data: {csrfmiddlewaretoken: token, email: email, password: password},
        success: function(data){
            if(data == 1){
                $('.alert').show();
                $('.alert').addClass('alert-danger');
                $('.alert').removeClass('alert-success');
                $('.alert').text('Такой логин уже занят!');
                 //$('.show_errors').html('Такой логин уже занят!');
            }else{

                $('.alert').show();
                $('.alert').addClass('alert-success');
                $('.alert').removeClass('alert-danger');
                $('.alert').text('Вы успешно зарегистрированы!');

                //alert('Вы успешно зарегистрированы!');
            }
       }
    });
});


$('#auth_btn').on('click', function(){
    let email = $('#email').val();
    let password = $('#password').val();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
            url: '/ajaxAuth',
            method: 'post',
            dataType: 'html',
            data: {csrfmiddlewaretoken: token, email: email, password: password},
            success: function(data){
                if(data == 4){
                    $('.alert').show();
                    $('.alert').addClass('alert-danger');
                    $('.alert').removeClass('alert-success');
                    $('.alert').text('Такой email не существует!');
                }
                else if(data == 1){
                    $('.alert').show();
                    $('.alert').addClass('alert-danger');
                    $('.alert').removeClass('alert-success');
                    $('.alert').text('Учетная запись не активирована!');
                }
                else if(data == 2){
                    $('.alert').show();
                    $('.alert').addClass('alert-danger');
                    $('.alert').removeClass('alert-success');
                    $('.alert').text('Неверный пароль!');
                }else{
                    alert('Вы успешно авторизированы!');
                    document.location.href='/profile';
                }
            }
    });
});

