<?php
    $success = 0;
    $uploadedFile = '';
    
    //File upload path
    $uploadPath = "uploads/";
    var_dump($_FILES);
    $targetPath = $uploadPath . basename($_FILES["files"]["name"]);

    if(@move_uploaded_file($_FILES['files']['tmp_name'], $targetPath)){
        $success = 1;
        $uploadedFile = $targetPath;
    }
    
    sleep(1);
?>
<script type="text/javascript">window.top.window.stopUpload(<?php echo $success; ?>,'<?php echo $uploadedFile; ?>');</script>