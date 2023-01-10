import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatSliderChange } from '@angular/material/slider';
import { MatSlideToggleChange } from '@angular/material/slide-toggle';
import { finalize } from 'rxjs';
import { FuseLoadingService } from '@fuse/services/loading';
import { FuseComponentsComponent } from 'app/modules/admin/ui/fuse-components/fuse-components.component';

@Component({
    selector   : 'loading-bar',
    templateUrl: './loading-bar.component.html'
})
export class LoadingBarComponent
{
    apiCallStatus: string = '-';
    mode: 'determinate' | 'indeterminate' = 'indeterminate';

    /**
     * Constructor
     */
    constructor(
        private _httpClient: HttpClient,
        private _fuseComponentsComponent: FuseComponentsComponent,
        private _fuseLoadingService: FuseLoadingService
    )
    {
    }

    // -----------------------------------------------------------------------------------------------------
    // @ Public methods
    // -----------------------------------------------------------------------------------------------------

    /**
     * Toggle the drawer
     */
    toggleDrawer(): void
    {
        // Toggle the drawer
        this._fuseComponentsComponent.matDrawer.toggle();
    }

    /**
     * Show the loading bar
     */
    showLoadingBar(): void
    {
        this._fuseLoadingService.show();
    }

    /**
     * Hide the loading bar
     */
    hideLoadingBar(): void
    {
        this._fuseLoadingService.hide();
    }

    /**
     * Set the auto mode
     *
     * @param change
     */
    setAutoMode(change: MatSlideToggleChange): void
    {
        this._fuseLoadingService.setAutoMode(change.checked);
    }

    /**
     * Make a fake API call
     */
    makeAPICall(): void
    {
        this.apiCallStatus = 'Waiting...';

        this._httpClient.get('https://jsonplaceholder.typicode.com/posts?_delay=2000')
            .pipe(finalize(() => {
                this.apiCallStatus = 'Finished!';
            }))
            .subscribe((response) => {
                console.log(response);
            });
    }

    /**
     * Toggle the mode
     */
    toggleMode(): void
    {
        // Show the loading bar
        this._fuseLoadingService.show();

        // Set the mode
        this.mode = this.mode === 'indeterminate' ? 'determinate' : 'indeterminate';
        this._fuseLoadingService.setMode(this.mode);
    }

    /**
     * Set the progress
     *
     * @param change
     */
    setProgress(change: MatSliderChange): void
    {
        this._fuseLoadingService.setProgress(change.value);
    }
}
