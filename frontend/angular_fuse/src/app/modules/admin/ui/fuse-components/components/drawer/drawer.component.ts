import { Component } from '@angular/core';
import { FuseDrawerMode } from '@fuse/components/drawer';
import { FuseComponentsComponent } from 'app/modules/admin/ui/fuse-components/fuse-components.component';

@Component({
    selector   : 'drawer',
    templateUrl: './drawer.component.html'
})
export class DrawerComponent
{
    drawerMode: FuseDrawerMode;
    drawerOpened: boolean;

    /**
     * Constructor
     */
    constructor(
        private _fuseComponentsComponent: FuseComponentsComponent
    )
    {
        // Set the defaults
        this.drawerMode = 'side';
        this.drawerOpened = true;
    }

    // -----------------------------------------------------------------------------------------------------
    // @ Public methods
    // -----------------------------------------------------------------------------------------------------

    /**
     * Toggle the drawer mode
     */
    toggleDrawerMode(): void
    {
        this.drawerMode = this.drawerMode === 'side' ? 'over' : 'side';
    }

    /**
     * Toggle the drawer open
     */
    toggleDrawerOpen(): void
    {
        this.drawerOpened = !this.drawerOpened;
    }

    /**
     * Drawer opened changed
     *
     * @param opened
     */
    drawerOpenedChanged(opened: boolean): void
    {
        this.drawerOpened = opened;
    }

    /**
     * Toggle the drawer
     */
    toggleDrawer(): void
    {
        // Toggle the drawer
        this._fuseComponentsComponent.matDrawer.toggle();
    }
}
