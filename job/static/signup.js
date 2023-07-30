<script>

    function passCheck()
    {
        if (document.signup.pwd.value!=document.signup.cpd.value)
        {
            alert('Please check again entered password and confirm password !!');
            document.signup.cpd.focus();
            return false;
        }
        return true;
    }

</script>