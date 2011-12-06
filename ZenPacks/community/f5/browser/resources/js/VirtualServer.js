/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');


/*
 * Friendly names for the components. First parameter is the meta_type in your
 * custom component class. Second parameter is the singular form of the
 * friendly name to be displayed in the UI. Third parameter is the plural form.
 */
ZC.registerName('BigipVirtualServer', _t('Virtual Server'), _t('Virtual Servers'));

/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componentType".
 */
ZC.BigipVirtualServerPanel = Ext.extend(ZC.ComponentGridPanel, {
	subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
        	autoExpandColumn: 'name',
            componentType: 'BigipVirtualServer',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'vsIP'},
                {name: 'ltmVirtualServPort'},
                {name: 'ltmVirtualServAddrRouteDomain'},
                {name: 'VsStatusEnabledState'},
                {name: 'VsStatusAvailState'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'vsIP',
                dataIndex: 'vsIP',
                header: _t('IP Address'),
                sortable: true,
                width: 100
            },{
                id: 'ltmVirtualServPort',
                dataIndex: 'ltmVirtualServPort',
                header: _t('Port'),
                sortable: true,
                width: 100
            },{
                id: 'ltmVirtualServAddrRouteDomain',
                dataIndex: 'ltmVirtualServAddrRouteDomain',
                header: _t('route-domain'),
                sortable: true,
                width: 100
            },{
                id: 'VsStatusEnabledState',
                dataIndex: 'VsStatusEnabledState',
                header: _t('Enabled/Disabled'),
                sortable: true,
                width: 100
            },{
                id: 'VsStatusAvailState',
                dataIndex: 'VsStatusAvailState',
                header: _t('Availability Status'),
                sortable: true,
                width: 200
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.BigipVirtualServerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BigipVirtualServerPanel', ZC.BigipVirtualServerPanel);


})();