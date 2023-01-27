import { Component, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { UntypedFormBuilder, UntypedFormGroup, NgForm, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { fuseAnimations } from '@fuse/animations';
import { FuseAlertType } from '@fuse/components/alert';
import { AuthService } from 'app/core/auth/auth.service';
import { HttpClient , HttpHeaders, HttpParams} from '@angular/common/http'; 
import { catchError } from 'rxjs/operators';



@Component({
    selector     : 'auth-sign-in',
    templateUrl  : './sign-in.component.html',
    encapsulation: ViewEncapsulation.None,
    animations   : fuseAnimations
})
export class AuthSignInComponent implements OnInit
{
    @ViewChild('signInNgForm') signInNgForm: NgForm;

    alert: { type: FuseAlertType; message: string } = {
        type   : 'success',
        message: ''
    };
    signInForm: UntypedFormGroup;
    showAlert: boolean = false;

    /**
     * Constructor
     */
    constructor(
        private _activatedRoute: ActivatedRoute,
        private _authService: AuthService,
        private _formBuilder: UntypedFormBuilder,
        private _router: Router,
        private http:HttpClient
    )
    {
    }

    // -----------------------------------------------------------------------------------------------------
    // @ Lifecycle hooks
    // -----------------------------------------------------------------------------------------------------

    /**
     * On init
     */
    ngOnInit(): void
    {
        // Create the form
        this.signInForm = this._formBuilder.group({
            username     : ['admin', [Validators.required]],
            password  : ['123456', Validators.required],
            rememberMe: ['']
        });
    }

    // -----------------------------------------------------------------------------------------------------
    // @ Public methods
    // -----------------------------------------------------------------------------------------------------

    /**
     * Sign in
     */
    signIn(): void
    {
        // Return if the form is invalid
        if ( this.signInForm.invalid )
        {
            return;
        }

        // Disable the form
        this.signInForm.disable();

        // Hide the alert
        this.showAlert = false;

        // Sign in  
        
        this._authService.signIn(this.signInForm.value).subscribe({
            complete: () => { 
                
             }, // completeHandler
            error: (respose:any) => { 
                
                debugger

                // Re-enable the form
                this.signInForm.enable();

                // Reset the form
                this.signInNgForm.resetForm();

                // Set the alert
                this.alert = {
                    type   : 'error',
                    message: respose[0]['message']
                };

                // Show the alert
                this.showAlert = true;
             },    // errorHandler 
            next: (respose:any) => {  
                
                
                    // Set the redirect url.
                    // The '/signed-in-redirect' is a dummy url to catch the request and redirect the user
                    // to the correct page after a successful sign in. This way, that url can be set via
                    // routing file and we don't have to touch here.
                    const redirectURL = this._activatedRoute.snapshot.queryParamMap.get('redirectURL') || '/signed-in-redirect';

                    // Navigate to the redirect url
                    this._router.navigateByUrl(redirectURL); 
            },     
        });


            // this._authService.signIn(this.signInForm.value).subscribe(
            //     () => {


            //         debugger
            //         // Set the redirect url.
            //         // The '/signed-in-redirect' is a dummy url to catch the request and redirect the user
            //         // to the correct page after a successful sign in. This way, that url can be set via
            //         // routing file and we don't have to touch here.
            //         const redirectURL = this._activatedRoute.snapshot.queryParamMap.get('redirectURL') || '/signed-in-redirect';

            //         // Navigate to the redirect url
            //         this._router.navigateByUrl(redirectURL);

            //     },
            //     (response) => {

            //         debugger

            //         // Re-enable the form
            //         this.signInForm.enable();

            //         // Reset the form
            //         this.signInNgForm.resetForm();

            //         // Set the alert
            //         this.alert = {
            //             type   : 'error',
            //             message: 'Wrong email or password'
            //         };

            //         // Show the alert
            //         this.showAlert = true;
            //     }
            // );
    }
}
