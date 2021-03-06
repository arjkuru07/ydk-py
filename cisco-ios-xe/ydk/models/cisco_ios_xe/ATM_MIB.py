""" ATM_MIB 

This is the MIB Module for ATM and AAL5\-related
objects for managing ATM interfaces, ATM virtual
links, ATM cross\-connects, AAL5 entities, and
and AAL5 connections.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ATMMIB(Entity):
    """
    
    
    .. attribute:: atmmibobjects
    
    	
    	**type**\:  :py:class:`AtmMIBObjects <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmMIBObjects>`
    
    	**config**\: False
    
    .. attribute:: atminterfaceconftable
    
    	This table contains ATM local interface configuration parameters, one entry per ATM interface port
    	**type**\:  :py:class:`AtmInterfaceConfTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceConfTable>`
    
    	**config**\: False
    
    .. attribute:: atminterfaceds3plcptable
    
    	This table contains ATM interface DS3 PLCP parameters and state variables, one entry per ATM interface port
    	**type**\:  :py:class:`AtmInterfaceDs3PlcpTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceDs3PlcpTable>`
    
    	**config**\: False
    
    .. attribute:: atminterfacetctable
    
    	This table contains ATM interface TC Sublayer parameters and state variables, one entry per ATM interface port
    	**type**\:  :py:class:`AtmInterfaceTCTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceTCTable>`
    
    	**config**\: False
    
    .. attribute:: atmtrafficdescrparamtable
    
    	This table contains information on ATM traffic descriptor type and the associated parameters
    	**type**\:  :py:class:`AtmTrafficDescrParamTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmTrafficDescrParamTable>`
    
    	**config**\: False
    
    .. attribute:: atmvpltable
    
    	The Virtual Path Link (VPL) table.  A bi\-directional VPL is modeled as one entry in this table. This table can be used for PVCs, SVCs and Soft PVCs. Entries are not present in this table for the VPIs used by entries in the atmVclTable
    	**type**\:  :py:class:`AtmVplTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVplTable>`
    
    	**config**\: False
    
    .. attribute:: atmvcltable
    
    	The Virtual Channel Link (VCL) table.  A bi\-directional VCL is modeled as one entry in this table. This table can be used for PVCs, SVCs and Soft PVCs
    	**type**\:  :py:class:`AtmVclTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable>`
    
    	**config**\: False
    
    .. attribute:: atmvpcrossconnecttable
    
    	The ATM VP Cross Connect table for PVCs. An entry in this table models two cross\-connected VPLs. Each VPL must have its atmConnKind set to pvc(1)
    	**type**\:  :py:class:`AtmVpCrossConnectTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVpCrossConnectTable>`
    
    	**config**\: False
    
    .. attribute:: atmvccrossconnecttable
    
    	The ATM VC Cross Connect table for PVCs. An entry in this table models two cross\-connected VCLs. Each VCL must have its atmConnKind set to pvc(1)
    	**type**\:  :py:class:`AtmVcCrossConnectTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVcCrossConnectTable>`
    
    	**config**\: False
    
    .. attribute:: aal5vcctable
    
    	This table contains AAL5 VCC performance parameters
    	**type**\:  :py:class:`Aal5VccTable <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Aal5VccTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ATM-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        super(ATMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "ATM-MIB"
        self.yang_parent_name = "ATM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("atmMIBObjects", ("atmmibobjects", ATMMIB.AtmMIBObjects)), ("atmInterfaceConfTable", ("atminterfaceconftable", ATMMIB.AtmInterfaceConfTable)), ("atmInterfaceDs3PlcpTable", ("atminterfaceds3plcptable", ATMMIB.AtmInterfaceDs3PlcpTable)), ("atmInterfaceTCTable", ("atminterfacetctable", ATMMIB.AtmInterfaceTCTable)), ("atmTrafficDescrParamTable", ("atmtrafficdescrparamtable", ATMMIB.AtmTrafficDescrParamTable)), ("atmVplTable", ("atmvpltable", ATMMIB.AtmVplTable)), ("atmVclTable", ("atmvcltable", ATMMIB.AtmVclTable)), ("atmVpCrossConnectTable", ("atmvpcrossconnecttable", ATMMIB.AtmVpCrossConnectTable)), ("atmVcCrossConnectTable", ("atmvccrossconnecttable", ATMMIB.AtmVcCrossConnectTable)), ("aal5VccTable", ("aal5vcctable", ATMMIB.Aal5VccTable))])
        self._leafs = OrderedDict()

        self.atmmibobjects = ATMMIB.AtmMIBObjects()
        self.atmmibobjects.parent = self
        self._children_name_map["atmmibobjects"] = "atmMIBObjects"

        self.atminterfaceconftable = ATMMIB.AtmInterfaceConfTable()
        self.atminterfaceconftable.parent = self
        self._children_name_map["atminterfaceconftable"] = "atmInterfaceConfTable"

        self.atminterfaceds3plcptable = ATMMIB.AtmInterfaceDs3PlcpTable()
        self.atminterfaceds3plcptable.parent = self
        self._children_name_map["atminterfaceds3plcptable"] = "atmInterfaceDs3PlcpTable"

        self.atminterfacetctable = ATMMIB.AtmInterfaceTCTable()
        self.atminterfacetctable.parent = self
        self._children_name_map["atminterfacetctable"] = "atmInterfaceTCTable"

        self.atmtrafficdescrparamtable = ATMMIB.AtmTrafficDescrParamTable()
        self.atmtrafficdescrparamtable.parent = self
        self._children_name_map["atmtrafficdescrparamtable"] = "atmTrafficDescrParamTable"

        self.atmvpltable = ATMMIB.AtmVplTable()
        self.atmvpltable.parent = self
        self._children_name_map["atmvpltable"] = "atmVplTable"

        self.atmvcltable = ATMMIB.AtmVclTable()
        self.atmvcltable.parent = self
        self._children_name_map["atmvcltable"] = "atmVclTable"

        self.atmvpcrossconnecttable = ATMMIB.AtmVpCrossConnectTable()
        self.atmvpcrossconnecttable.parent = self
        self._children_name_map["atmvpcrossconnecttable"] = "atmVpCrossConnectTable"

        self.atmvccrossconnecttable = ATMMIB.AtmVcCrossConnectTable()
        self.atmvccrossconnecttable.parent = self
        self._children_name_map["atmvccrossconnecttable"] = "atmVcCrossConnectTable"

        self.aal5vcctable = ATMMIB.Aal5VccTable()
        self.aal5vcctable.parent = self
        self._children_name_map["aal5vcctable"] = "aal5VccTable"
        self._segment_path = lambda: "ATM-MIB:ATM-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ATMMIB, [], name, value)


    class AtmMIBObjects(Entity):
        """
        
        
        .. attribute:: atmvpcrossconnectindexnext
        
        	This object contains an appropriate value to be used for atmVpCrossConnectIndex when creating entries in the atmVpCrossConnectTable.  The value 0 indicates that no unassigned entries are available. To obtain the atmVpCrossConnectIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object.  After each retrieval, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: atmvccrossconnectindexnext
        
        	This object contains an appropriate value to be used for atmVcCrossConnectIndex when creating entries in the atmVcCrossConnectTable.  The value 0 indicates that no unassigned entries are available. To obtain the atmVcCrossConnectIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object.  After each retrieval, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: atmtrafficdescrparamindexnext
        
        	This object contains an appropriate value to be used for atmTrafficDescrParamIndex when creating entries in the atmTrafficDescrParamTable. The value 0 indicates that no unassigned entries are available. To obtain the atmTrafficDescrParamIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object.  After each retrieval, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmMIBObjects, self).__init__()

            self.yang_name = "atmMIBObjects"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('atmvpcrossconnectindexnext', (YLeaf(YType.int32, 'atmVpCrossConnectIndexNext'), ['int'])),
                ('atmvccrossconnectindexnext', (YLeaf(YType.int32, 'atmVcCrossConnectIndexNext'), ['int'])),
                ('atmtrafficdescrparamindexnext', (YLeaf(YType.int32, 'atmTrafficDescrParamIndexNext'), ['int'])),
            ])
            self.atmvpcrossconnectindexnext = None
            self.atmvccrossconnectindexnext = None
            self.atmtrafficdescrparamindexnext = None
            self._segment_path = lambda: "atmMIBObjects"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmMIBObjects, [u'atmvpcrossconnectindexnext', u'atmvccrossconnectindexnext', u'atmtrafficdescrparamindexnext'], name, value)



    class AtmInterfaceConfTable(Entity):
        """
        This table contains ATM local interface
        configuration parameters, one entry per ATM
        interface port.
        
        .. attribute:: atminterfaceconfentry
        
        	This list contains ATM interface configuration parameters and state variables and is indexed by ifIndex values of ATM interfaces
        	**type**\: list of  		 :py:class:`AtmInterfaceConfEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmInterfaceConfTable, self).__init__()

            self.yang_name = "atmInterfaceConfTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmInterfaceConfEntry", ("atminterfaceconfentry", ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry))])
            self._leafs = OrderedDict()

            self.atminterfaceconfentry = YList(self)
            self._segment_path = lambda: "atmInterfaceConfTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmInterfaceConfTable, [], name, value)


        class AtmInterfaceConfEntry(Entity):
            """
            This list contains ATM interface configuration
            parameters and state variables and is indexed
            by ifIndex values of ATM interfaces.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atminterfacemaxvpcs
            
            	The maximum number of VPCs (PVPCs and SVPCs) supported at this ATM interface. At the ATM UNI, the maximum number of VPCs (PVPCs and SVPCs) ranges from 0 to 256 only
            	**type**\: int
            
            	**range:** 0..4096
            
            	**config**\: False
            
            .. attribute:: atminterfacemaxvccs
            
            	The maximum number of VCCs (PVCCs and SVCCs) supported at this ATM interface
            	**type**\: int
            
            	**range:** 0..65536
            
            	**config**\: False
            
            .. attribute:: atminterfaceconfvpcs
            
            	The number of VPCs (PVPC, Soft PVPC and SVPC) currently in use at this ATM interface.  It includes the number of PVPCs and Soft PVPCs that are configured at the interface, plus the number of SVPCs that are currently  established at the interface.  At the ATM UNI, the configured number of VPCs (PVPCs and SVPCs) can range from 0 to 256 only
            	**type**\: int
            
            	**range:** 0..4096
            
            	**config**\: False
            
            .. attribute:: atminterfaceconfvccs
            
            	The number of VCCs (PVCC, Soft PVCC and SVCC) currently in use at this ATM interface.  It includes the number of PVCCs and Soft PVCCs that are configured at the interface, plus the number of SVCCs that are currently  established at the interface
            	**type**\: int
            
            	**range:** 0..65536
            
            	**config**\: False
            
            .. attribute:: atminterfacemaxactivevpibits
            
            	The  maximum number of active VPI bits configured for use at the ATM interface. At the ATM UNI, the maximum number of active VPI bits configured for use ranges from 0 to 8 only
            	**type**\: int
            
            	**range:** 0..12
            
            	**config**\: False
            
            .. attribute:: atminterfacemaxactivevcibits
            
            	The maximum number of active VCI bits configured for use at this ATM interface
            	**type**\: int
            
            	**range:** 0..16
            
            	**config**\: False
            
            .. attribute:: atminterfaceilmivpi
            
            	The VPI value of the VCC supporting the ILMI at this ATM interface.  If the values of atmInterfaceIlmiVpi and atmInterfaceIlmiVci are both equal to zero then the ILMI is not supported at this ATM interface
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: atminterfaceilmivci
            
            	The VCI value of the VCC supporting the ILMI at this ATM interface.  If the values of atmInterfaceIlmiVpi and atmInterfaceIlmiVci are both equal to zero then the ILMI is not supported at this ATM interface
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: atminterfaceaddresstype
            
            	The type of primary ATM address configured for use at this ATM interface
            	**type**\:  :py:class:`AtmInterfaceAddressType <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry.AtmInterfaceAddressType>`
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: atminterfaceadminaddress
            
            	The primary address assigned for administrative purposes, for example, an address associated with the service provider side of a public network UNI (thus, the value of this address corresponds with the value of ifPhysAddress at the host side). If this interface has no assigned administrative address, or when the address used for administrative purposes is the same as that used for ifPhysAddress, then this is an octet string of zero length
            	**type**\: str
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: atminterfacemyneighboripaddress
            
            	The IP address of the neighbor system connected to the  far end of this interface, to which a Network Management Station can send SNMP messages, as IP datagrams sent to UDP port 161, in order to access network management information concerning the operation of that system.  Note that the value of this object may be obtained in different ways, e.g., by manual configuration, or through ILMI interaction with the neighbor system
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: atminterfacemyneighborifname
            
            	The textual name of the interface on the neighbor system on the far end of this interface, and to which this interface connects.  If the neighbor system is manageable through SNMP and supports the object ifName, the value of this object must be identical with that of ifName for the ifEntry of the lowest level physical interface for this port.  If this interface does not have a textual name, the value of this object is a zero length string.  Note that the value of this object may be obtained in different ways, e.g., by manual configuration, or through ILMI interaction with the neighbor system
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: atminterfacecurrentmaxvpibits
            
            	The maximum number of VPI Bits that may currently be used at this ATM interface. The value is the minimum of atmInterfaceMaxActiveVpiBits, and the atmInterfaceMaxActiveVpiBits of the interface's UNI/NNI peer.  If the interface does not negotiate with its peer to determine the number of VPI Bits that can be used on the interface, then the value of this object must equal atmInterfaceMaxActiveVpiBits
            	**type**\: int
            
            	**range:** 0..12
            
            	**config**\: False
            
            .. attribute:: atminterfacecurrentmaxvcibits
            
            	The maximum number of VCI Bits that may currently be used at this ATM interface. The value is the minimum of atmInterfaceMaxActiveVciBits, and the atmInterfaceMaxActiveVciBits of the interface's UNI/NNI peer.  If the interface does not negotiate with its peer to determine the number of VCI Bits that can be used on the interface, then the value of this object must equal atmInterfaceMaxActiveVciBits
            	**type**\: int
            
            	**range:** 0..16
            
            	**config**\: False
            
            .. attribute:: atminterfacesubscraddress
            
            	The identifier assigned by a service provider to the network side of a public network UNI. If this interface has no assigned service provider address, or for other interfaces this is an octet string of zero length
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: atmintfcurrentlydowntouppvcls
            
            	The current number PVCLs on this interface which  changed state to 'up' since the last  atmIntPvcUpTrap was sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmintfoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the oam loopback failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmintfcurrentlyoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the oam loop back has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmintfpvcfailures
            
            	The number of times the operational status of a PVCL on this interface has gone down
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmintfcurrentlyfailingpvcls
            
            	The current number of VCLs on this interface for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmintfpvcfailurestrapenable
            
            	Allows the generation of traps in response to PVCL failures on this interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: atmintfpvcnotificationinterval
            
            	The minimum interval between the sending of cIntfPvcFailuresTrap notifications for this interface
            	**type**\: int
            
            	**range:** 1..3600
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: atmpreviouslyfailedpvclinterval
            
            	The interval for storing the failed time in atmPreviouslyFailedPVclTimeStamp
            	**type**\: int
            
            	**range:** 0..3600
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: catmintfcurrentlydowntouppvcls
            
            	The current number PVCLs on this interface which  changed state to 'up' since the last  atmIntPvcUp2Trap was sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the OAM loopback failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcurrentoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the OAM loop back has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfsegccoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the Segment CC OAM failed condition  but the status of each PVCL remain in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcursegccoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the Segment CC OAM has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfendccoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the End\-to\-End CC OAM failed condition  but the status of each PVCL remain in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcurendccoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the End\-to\-End CC OAM has failed but the status of each PVCL  remain in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfaisrdioamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the AIS RDI OAM failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcuraisrdioamfailingpvcls
            
            	The current number of PVCLs on this interface for which the AIS RDI OAM has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfanyoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in any type of OAM failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcuranyoamfailingpvcls
            
            	The current number of PVCLs on this interface for which  any of OAM has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintftypeofoamfailure
            
            	Type of OAM failure
            	**type**\:  :py:class:`CatmOAMFailureType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMFailureType>`
            
            	**config**\: False
            
            .. attribute:: catmintfoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the OAM loopback recovered condition and  the status of each PVCL is in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcurrentoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the OAM loop back has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfsegccoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the Segment CC OAM recovered condition  and the status of each PVCL is in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcursegccoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the Segment CC OAM has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfendccoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the End\-to\-End CC OAM recovered condition  and the status of each PVCL is in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcurendccoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the End\-to\-End CC OAM has recovered and the status of each PVCL  is in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfaisrdioamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the AIS RDI OAM recovered condition and  the status of each PVCL is in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcuraisrdioamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the AIS RDI OAM has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfanyoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in any type of OAM recovered condition and  the status of each PVCL is in the 'up' state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintfcuranyoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which  any of OAM has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmintftypeofoamrecover
            
            	Type of OAM Recovered
            	**type**\:  :py:class:`CatmOAMRecoveryType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMRecoveryType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry, self).__init__()

                self.yang_name = "atmInterfaceConfEntry"
                self.yang_parent_name = "atmInterfaceConfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atminterfacemaxvpcs', (YLeaf(YType.int32, 'atmInterfaceMaxVpcs'), ['int'])),
                    ('atminterfacemaxvccs', (YLeaf(YType.int32, 'atmInterfaceMaxVccs'), ['int'])),
                    ('atminterfaceconfvpcs', (YLeaf(YType.int32, 'atmInterfaceConfVpcs'), ['int'])),
                    ('atminterfaceconfvccs', (YLeaf(YType.int32, 'atmInterfaceConfVccs'), ['int'])),
                    ('atminterfacemaxactivevpibits', (YLeaf(YType.int32, 'atmInterfaceMaxActiveVpiBits'), ['int'])),
                    ('atminterfacemaxactivevcibits', (YLeaf(YType.int32, 'atmInterfaceMaxActiveVciBits'), ['int'])),
                    ('atminterfaceilmivpi', (YLeaf(YType.int32, 'atmInterfaceIlmiVpi'), ['int'])),
                    ('atminterfaceilmivci', (YLeaf(YType.int32, 'atmInterfaceIlmiVci'), ['int'])),
                    ('atminterfaceaddresstype', (YLeaf(YType.enumeration, 'atmInterfaceAddressType'), [('ydk.models.cisco_ios_xe.ATM_MIB', 'ATMMIB', 'AtmInterfaceConfTable.AtmInterfaceConfEntry.AtmInterfaceAddressType')])),
                    ('atminterfaceadminaddress', (YLeaf(YType.str, 'atmInterfaceAdminAddress'), ['str'])),
                    ('atminterfacemyneighboripaddress', (YLeaf(YType.str, 'atmInterfaceMyNeighborIpAddress'), ['str'])),
                    ('atminterfacemyneighborifname', (YLeaf(YType.str, 'atmInterfaceMyNeighborIfName'), ['str'])),
                    ('atminterfacecurrentmaxvpibits', (YLeaf(YType.int32, 'atmInterfaceCurrentMaxVpiBits'), ['int'])),
                    ('atminterfacecurrentmaxvcibits', (YLeaf(YType.int32, 'atmInterfaceCurrentMaxVciBits'), ['int'])),
                    ('atminterfacesubscraddress', (YLeaf(YType.str, 'atmInterfaceSubscrAddress'), ['str'])),
                    ('atmintfcurrentlydowntouppvcls', (YLeaf(YType.uint32, 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmIntfCurrentlyDownToUpPVcls'), ['int'])),
                    ('atmintfoamfailedpvcls', (YLeaf(YType.uint32, 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmIntfOAMFailedPVcls'), ['int'])),
                    ('atmintfcurrentlyoamfailingpvcls', (YLeaf(YType.uint32, 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmIntfCurrentlyOAMFailingPVcls'), ['int'])),
                    ('atmintfpvcfailures', (YLeaf(YType.uint32, 'CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfPvcFailures'), ['int'])),
                    ('atmintfcurrentlyfailingpvcls', (YLeaf(YType.uint32, 'CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfCurrentlyFailingPVcls'), ['int'])),
                    ('atmintfpvcfailurestrapenable', (YLeaf(YType.boolean, 'CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfPvcFailuresTrapEnable'), ['bool'])),
                    ('atmintfpvcnotificationinterval', (YLeaf(YType.int32, 'CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfPvcNotificationInterval'), ['int'])),
                    ('atmpreviouslyfailedpvclinterval', (YLeaf(YType.int32, 'CISCO-IETF-ATM2-PVCTRAP-MIB:atmPreviouslyFailedPVclInterval'), ['int'])),
                    ('catmintfcurrentlydowntouppvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurrentlyDownToUpPVcls'), ['int'])),
                    ('catmintfoamfailedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfOAMFailedPVcls'), ['int'])),
                    ('catmintfcurrentoamfailingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurrentOAMFailingPVcls'), ['int'])),
                    ('catmintfsegccoamfailedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfSegCCOAMFailedPVcls'), ['int'])),
                    ('catmintfcursegccoamfailingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurSegCCOAMFailingPVcls'), ['int'])),
                    ('catmintfendccoamfailedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfEndCCOAMFailedPVcls'), ['int'])),
                    ('catmintfcurendccoamfailingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurEndCCOAMFailingPVcls'), ['int'])),
                    ('catmintfaisrdioamfailedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAISRDIOAMFailedPVcls'), ['int'])),
                    ('catmintfcuraisrdioamfailingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAISRDIOAMFailingPVcls'), ['int'])),
                    ('catmintfanyoamfailedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAnyOAMFailedPVcls'), ['int'])),
                    ('catmintfcuranyoamfailingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAnyOAMFailingPVcls'), ['int'])),
                    ('catmintftypeofoamfailure', (YLeaf(YType.enumeration, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfTypeOfOAMFailure'), [('ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMFailureType', '')])),
                    ('catmintfoamrcovedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfOAMRcovedPVcls'), ['int'])),
                    ('catmintfcurrentoamrcovingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurrentOAMRcovingPVcls'), ['int'])),
                    ('catmintfsegccoamrcovedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfSegCCOAMRcovedPVcls'), ['int'])),
                    ('catmintfcursegccoamrcovingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurSegCCOAMRcovingPVcls'), ['int'])),
                    ('catmintfendccoamrcovedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfEndCCOAMRcovedPVcls'), ['int'])),
                    ('catmintfcurendccoamrcovingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurEndCCOAMRcovingPVcls'), ['int'])),
                    ('catmintfaisrdioamrcovedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAISRDIOAMRcovedPVcls'), ['int'])),
                    ('catmintfcuraisrdioamrcovingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAISRDIOAMRcovingPVcls'), ['int'])),
                    ('catmintfanyoamrcovedpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAnyOAMRcovedPVcls'), ['int'])),
                    ('catmintfcuranyoamrcovingpvcls', (YLeaf(YType.uint32, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAnyOAMRcovingPVcls'), ['int'])),
                    ('catmintftypeofoamrecover', (YLeaf(YType.enumeration, 'CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfTypeOfOAMRecover'), [('ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMRecoveryType', '')])),
                ])
                self.ifindex = None
                self.atminterfacemaxvpcs = None
                self.atminterfacemaxvccs = None
                self.atminterfaceconfvpcs = None
                self.atminterfaceconfvccs = None
                self.atminterfacemaxactivevpibits = None
                self.atminterfacemaxactivevcibits = None
                self.atminterfaceilmivpi = None
                self.atminterfaceilmivci = None
                self.atminterfaceaddresstype = None
                self.atminterfaceadminaddress = None
                self.atminterfacemyneighboripaddress = None
                self.atminterfacemyneighborifname = None
                self.atminterfacecurrentmaxvpibits = None
                self.atminterfacecurrentmaxvcibits = None
                self.atminterfacesubscraddress = None
                self.atmintfcurrentlydowntouppvcls = None
                self.atmintfoamfailedpvcls = None
                self.atmintfcurrentlyoamfailingpvcls = None
                self.atmintfpvcfailures = None
                self.atmintfcurrentlyfailingpvcls = None
                self.atmintfpvcfailurestrapenable = None
                self.atmintfpvcnotificationinterval = None
                self.atmpreviouslyfailedpvclinterval = None
                self.catmintfcurrentlydowntouppvcls = None
                self.catmintfoamfailedpvcls = None
                self.catmintfcurrentoamfailingpvcls = None
                self.catmintfsegccoamfailedpvcls = None
                self.catmintfcursegccoamfailingpvcls = None
                self.catmintfendccoamfailedpvcls = None
                self.catmintfcurendccoamfailingpvcls = None
                self.catmintfaisrdioamfailedpvcls = None
                self.catmintfcuraisrdioamfailingpvcls = None
                self.catmintfanyoamfailedpvcls = None
                self.catmintfcuranyoamfailingpvcls = None
                self.catmintftypeofoamfailure = None
                self.catmintfoamrcovedpvcls = None
                self.catmintfcurrentoamrcovingpvcls = None
                self.catmintfsegccoamrcovedpvcls = None
                self.catmintfcursegccoamrcovingpvcls = None
                self.catmintfendccoamrcovedpvcls = None
                self.catmintfcurendccoamrcovingpvcls = None
                self.catmintfaisrdioamrcovedpvcls = None
                self.catmintfcuraisrdioamrcovingpvcls = None
                self.catmintfanyoamrcovedpvcls = None
                self.catmintfcuranyoamrcovingpvcls = None
                self.catmintftypeofoamrecover = None
                self._segment_path = lambda: "atmInterfaceConfEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmInterfaceConfTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry, [u'ifindex', u'atminterfacemaxvpcs', u'atminterfacemaxvccs', u'atminterfaceconfvpcs', u'atminterfaceconfvccs', u'atminterfacemaxactivevpibits', u'atminterfacemaxactivevcibits', u'atminterfaceilmivpi', u'atminterfaceilmivci', u'atminterfaceaddresstype', u'atminterfaceadminaddress', u'atminterfacemyneighboripaddress', u'atminterfacemyneighborifname', u'atminterfacecurrentmaxvpibits', u'atminterfacecurrentmaxvcibits', u'atminterfacesubscraddress', 'atmintfcurrentlydowntouppvcls', 'atmintfoamfailedpvcls', 'atmintfcurrentlyoamfailingpvcls', u'atmintfpvcfailures', u'atmintfcurrentlyfailingpvcls', u'atmintfpvcfailurestrapenable', u'atmintfpvcnotificationinterval', u'atmpreviouslyfailedpvclinterval', 'catmintfcurrentlydowntouppvcls', 'catmintfoamfailedpvcls', 'catmintfcurrentoamfailingpvcls', 'catmintfsegccoamfailedpvcls', 'catmintfcursegccoamfailingpvcls', 'catmintfendccoamfailedpvcls', 'catmintfcurendccoamfailingpvcls', 'catmintfaisrdioamfailedpvcls', 'catmintfcuraisrdioamfailingpvcls', 'catmintfanyoamfailedpvcls', 'catmintfcuranyoamfailingpvcls', 'catmintftypeofoamfailure', 'catmintfoamrcovedpvcls', 'catmintfcurrentoamrcovingpvcls', 'catmintfsegccoamrcovedpvcls', 'catmintfcursegccoamrcovingpvcls', 'catmintfendccoamrcovedpvcls', 'catmintfcurendccoamrcovingpvcls', 'catmintfaisrdioamrcovedpvcls', 'catmintfcuraisrdioamrcovingpvcls', 'catmintfanyoamrcovedpvcls', 'catmintfcuranyoamrcovingpvcls', 'catmintftypeofoamrecover'], name, value)

            class AtmInterfaceAddressType(Enum):
                """
                AtmInterfaceAddressType (Enum Class)

                The type of primary ATM address configured

                for use at this ATM interface.

                .. data:: private = 1

                .. data:: nsapE164 = 2

                .. data:: nativeE164 = 3

                .. data:: other = 4

                """

                private = Enum.YLeaf(1, "private")

                nsapE164 = Enum.YLeaf(2, "nsapE164")

                nativeE164 = Enum.YLeaf(3, "nativeE164")

                other = Enum.YLeaf(4, "other")





    class AtmInterfaceDs3PlcpTable(Entity):
        """
        This table contains ATM interface DS3 PLCP
        parameters and state variables, one entry per
        ATM interface port.
        
        .. attribute:: atminterfaceds3plcpentry
        
        	This list contains DS3 PLCP parameters and state variables at the ATM interface and is indexed by the ifIndex value of the ATM interface
        	**type**\: list of  		 :py:class:`AtmInterfaceDs3PlcpEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmInterfaceDs3PlcpTable, self).__init__()

            self.yang_name = "atmInterfaceDs3PlcpTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmInterfaceDs3PlcpEntry", ("atminterfaceds3plcpentry", ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry))])
            self._leafs = OrderedDict()

            self.atminterfaceds3plcpentry = YList(self)
            self._segment_path = lambda: "atmInterfaceDs3PlcpTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmInterfaceDs3PlcpTable, [], name, value)


        class AtmInterfaceDs3PlcpEntry(Entity):
            """
            This list contains DS3 PLCP parameters and
            state variables at the ATM interface and is
            indexed by the ifIndex value of the ATM interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atminterfaceds3plcpsefss
            
            	The number of DS3 PLCP Severely Errored Framing Seconds (SEFS). Each SEFS represents a one\-second interval which contains one or more SEF events
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atminterfaceds3plcpalarmstate
            
            	This variable indicates if there is an alarm present for the DS3 PLCP.  The value receivedFarEndAlarm means that the DS3 PLCP has received an incoming Yellow Signal, the value incomingLOF means that the DS3 PLCP has declared a loss of frame (LOF) failure condition, and the value noAlarm means that there are no alarms present. Transition from the failure to the no alarm state occurs when no defects (e.g., LOF) are received for more than 10 seconds
            	**type**\:  :py:class:`AtmInterfaceDs3PlcpAlarmState <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry.AtmInterfaceDs3PlcpAlarmState>`
            
            	**config**\: False
            
            .. attribute:: atminterfaceds3plcpuass
            
            	The counter associated with the number of Unavailable Seconds encountered by the PLCP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry, self).__init__()

                self.yang_name = "atmInterfaceDs3PlcpEntry"
                self.yang_parent_name = "atmInterfaceDs3PlcpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atminterfaceds3plcpsefss', (YLeaf(YType.uint32, 'atmInterfaceDs3PlcpSEFSs'), ['int'])),
                    ('atminterfaceds3plcpalarmstate', (YLeaf(YType.enumeration, 'atmInterfaceDs3PlcpAlarmState'), [('ydk.models.cisco_ios_xe.ATM_MIB', 'ATMMIB', 'AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry.AtmInterfaceDs3PlcpAlarmState')])),
                    ('atminterfaceds3plcpuass', (YLeaf(YType.uint32, 'atmInterfaceDs3PlcpUASs'), ['int'])),
                ])
                self.ifindex = None
                self.atminterfaceds3plcpsefss = None
                self.atminterfaceds3plcpalarmstate = None
                self.atminterfaceds3plcpuass = None
                self._segment_path = lambda: "atmInterfaceDs3PlcpEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmInterfaceDs3PlcpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry, [u'ifindex', u'atminterfaceds3plcpsefss', u'atminterfaceds3plcpalarmstate', u'atminterfaceds3plcpuass'], name, value)

            class AtmInterfaceDs3PlcpAlarmState(Enum):
                """
                AtmInterfaceDs3PlcpAlarmState (Enum Class)

                This variable indicates if there is an

                alarm present for the DS3 PLCP.  The value

                receivedFarEndAlarm means that the DS3 PLCP

                has received an incoming Yellow

                Signal, the value incomingLOF means that

                the DS3 PLCP has declared a loss of frame (LOF)

                failure condition, and the value noAlarm

                means that there are no alarms present.

                Transition from the failure to the no alarm state

                occurs when no defects (e.g., LOF) are received

                for more than 10 seconds.

                .. data:: noAlarm = 1

                .. data:: receivedFarEndAlarm = 2

                .. data:: incomingLOF = 3

                """

                noAlarm = Enum.YLeaf(1, "noAlarm")

                receivedFarEndAlarm = Enum.YLeaf(2, "receivedFarEndAlarm")

                incomingLOF = Enum.YLeaf(3, "incomingLOF")





    class AtmInterfaceTCTable(Entity):
        """
        This table contains ATM interface TC
        Sublayer parameters and state variables,
        one entry per ATM interface port.
        
        .. attribute:: atminterfacetcentry
        
        	This list contains TC Sublayer parameters and state variables at the ATM interface and is indexed by the ifIndex value of the ATM interface
        	**type**\: list of  		 :py:class:`AtmInterfaceTCEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmInterfaceTCTable, self).__init__()

            self.yang_name = "atmInterfaceTCTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmInterfaceTCEntry", ("atminterfacetcentry", ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry))])
            self._leafs = OrderedDict()

            self.atminterfacetcentry = YList(self)
            self._segment_path = lambda: "atmInterfaceTCTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmInterfaceTCTable, [], name, value)


        class AtmInterfaceTCEntry(Entity):
            """
            This list contains TC Sublayer parameters
            and state variables at the ATM interface and is
            indexed by the ifIndex value of the ATM interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atminterfaceocdevents
            
            	The number of times the Out of Cell Delineation (OCD) events occur.  If seven consecutive ATM cells have Header Error Control (HEC) violations, an OCD event occurs. A high number of OCD events may indicate a problem with the TC Sublayer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atminterfacetcalarmstate
            
            	This variable indicates if there is an alarm present for the TC Sublayer.  The value lcdFailure(2) indicates that the TC Sublayer is currently in the Loss of Cell Delineation (LCD) defect maintenance state.  The value noAlarm(1) indicates that the TC Sublayer is currently not in the LCD defect maintenance state
            	**type**\:  :py:class:`AtmInterfaceTCAlarmState <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry.AtmInterfaceTCAlarmState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry, self).__init__()

                self.yang_name = "atmInterfaceTCEntry"
                self.yang_parent_name = "atmInterfaceTCTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atminterfaceocdevents', (YLeaf(YType.uint32, 'atmInterfaceOCDEvents'), ['int'])),
                    ('atminterfacetcalarmstate', (YLeaf(YType.enumeration, 'atmInterfaceTCAlarmState'), [('ydk.models.cisco_ios_xe.ATM_MIB', 'ATMMIB', 'AtmInterfaceTCTable.AtmInterfaceTCEntry.AtmInterfaceTCAlarmState')])),
                ])
                self.ifindex = None
                self.atminterfaceocdevents = None
                self.atminterfacetcalarmstate = None
                self._segment_path = lambda: "atmInterfaceTCEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmInterfaceTCTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry, [u'ifindex', u'atminterfaceocdevents', u'atminterfacetcalarmstate'], name, value)

            class AtmInterfaceTCAlarmState(Enum):
                """
                AtmInterfaceTCAlarmState (Enum Class)

                This variable indicates if there is an

                alarm present for the TC Sublayer.  The value

                lcdFailure(2) indicates that the TC Sublayer

                is currently in the Loss of Cell Delineation

                (LCD) defect maintenance state.  The value

                noAlarm(1) indicates that the TC Sublayer

                is currently not in the LCD defect

                maintenance state.

                .. data:: noAlarm = 1

                .. data:: lcdFailure = 2

                """

                noAlarm = Enum.YLeaf(1, "noAlarm")

                lcdFailure = Enum.YLeaf(2, "lcdFailure")





    class AtmTrafficDescrParamTable(Entity):
        """
        This table contains information on ATM traffic
        descriptor type and the associated parameters.
        
        .. attribute:: atmtrafficdescrparamentry
        
        	This list contains ATM traffic descriptor type and the associated parameters
        	**type**\: list of  		 :py:class:`AtmTrafficDescrParamEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmTrafficDescrParamTable, self).__init__()

            self.yang_name = "atmTrafficDescrParamTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmTrafficDescrParamEntry", ("atmtrafficdescrparamentry", ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry))])
            self._leafs = OrderedDict()

            self.atmtrafficdescrparamentry = YList(self)
            self._segment_path = lambda: "atmTrafficDescrParamTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmTrafficDescrParamTable, [], name, value)


        class AtmTrafficDescrParamEntry(Entity):
            """
            This list contains ATM traffic descriptor
            type and the associated parameters.
            
            .. attribute:: atmtrafficdescrparamindex  (key)
            
            	This object is used by the virtual link table (i.e., VPL or VCL table) to identify the row of this table. When creating a new row in the table the value of this index may be obtained by retrieving the value of atmTrafficDescrParamIndexNext
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: atmtrafficdescrtype
            
            	The value of this object identifies the type of ATM traffic descriptor. The type may indicate no traffic descriptor or traffic descriptor with one or more parameters. These parameters are specified as a parameter vector, in the corresponding instances of the objects\:     atmTrafficDescrParam1     atmTrafficDescrParam2     atmTrafficDescrParam3     atmTrafficDescrParam4     atmTrafficDescrParam5
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: atmtrafficdescrparam1
            
            	The first parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: atmtrafficdescrparam2
            
            	The second parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: atmtrafficdescrparam3
            
            	The third parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: atmtrafficdescrparam4
            
            	The fourth parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: atmtrafficdescrparam5
            
            	The fifth parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: atmtrafficqosclass
            
            	The value of this object identifies the QoS Class. Four Service classes have been specified in the ATM Forum UNI Specification\: Service Class A\: Constant bit rate video and                  Circuit emulation Service Class B\: Variable bit rate video/audio Service Class C\: Connection\-oriented data Service Class D\: Connectionless data Four QoS classes numbered 1, 2, 3, and 4 have been specified with the aim to support service classes A, B, C, and D respectively. An unspecified QoS Class numbered `0' is used for best effort traffic
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: atmtrafficdescrrowstatus
            
            	This object is used to create a new row or modify or delete an existing row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: atmservicecategory
            
            	The ATM service category
            	**type**\:  :py:class:`AtmServiceCategory <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmServiceCategory>`
            
            	**config**\: False
            
            .. attribute:: atmtrafficframediscard
            
            	If set to 'true', this object indicates that the network is requested to treat data for this connection, in the given direction, as frames (e.g. AAL5 CPCS\_PDU's) rather than as individual cells.  While the precise implementation is network\-specific, this treatment may for example involve discarding entire frames during congestion, rather than a few cells from many frames
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry, self).__init__()

                self.yang_name = "atmTrafficDescrParamEntry"
                self.yang_parent_name = "atmTrafficDescrParamTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['atmtrafficdescrparamindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('atmtrafficdescrparamindex', (YLeaf(YType.int32, 'atmTrafficDescrParamIndex'), ['int'])),
                    ('atmtrafficdescrtype', (YLeaf(YType.str, 'atmTrafficDescrType'), ['str'])),
                    ('atmtrafficdescrparam1', (YLeaf(YType.int32, 'atmTrafficDescrParam1'), ['int'])),
                    ('atmtrafficdescrparam2', (YLeaf(YType.int32, 'atmTrafficDescrParam2'), ['int'])),
                    ('atmtrafficdescrparam3', (YLeaf(YType.int32, 'atmTrafficDescrParam3'), ['int'])),
                    ('atmtrafficdescrparam4', (YLeaf(YType.int32, 'atmTrafficDescrParam4'), ['int'])),
                    ('atmtrafficdescrparam5', (YLeaf(YType.int32, 'atmTrafficDescrParam5'), ['int'])),
                    ('atmtrafficqosclass', (YLeaf(YType.int32, 'atmTrafficQoSClass'), ['int'])),
                    ('atmtrafficdescrrowstatus', (YLeaf(YType.enumeration, 'atmTrafficDescrRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('atmservicecategory', (YLeaf(YType.enumeration, 'atmServiceCategory'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmServiceCategory', '')])),
                    ('atmtrafficframediscard', (YLeaf(YType.boolean, 'atmTrafficFrameDiscard'), ['bool'])),
                ])
                self.atmtrafficdescrparamindex = None
                self.atmtrafficdescrtype = None
                self.atmtrafficdescrparam1 = None
                self.atmtrafficdescrparam2 = None
                self.atmtrafficdescrparam3 = None
                self.atmtrafficdescrparam4 = None
                self.atmtrafficdescrparam5 = None
                self.atmtrafficqosclass = None
                self.atmtrafficdescrrowstatus = None
                self.atmservicecategory = None
                self.atmtrafficframediscard = None
                self._segment_path = lambda: "atmTrafficDescrParamEntry" + "[atmTrafficDescrParamIndex='" + str(self.atmtrafficdescrparamindex) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmTrafficDescrParamTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry, [u'atmtrafficdescrparamindex', u'atmtrafficdescrtype', u'atmtrafficdescrparam1', u'atmtrafficdescrparam2', u'atmtrafficdescrparam3', u'atmtrafficdescrparam4', u'atmtrafficdescrparam5', u'atmtrafficqosclass', u'atmtrafficdescrrowstatus', u'atmservicecategory', u'atmtrafficframediscard'], name, value)




    class AtmVplTable(Entity):
        """
        The Virtual Path Link (VPL) table.  A
        bi\-directional VPL is modeled as one entry
        in this table. This table can be used for
        PVCs, SVCs and Soft PVCs.
        Entries are not present in this table for
        the VPIs used by entries in the atmVclTable.
        
        .. attribute:: atmvplentry
        
        	An entry in the VPL table.  This entry is used to model a bi\-directional VPL. To create a VPL at an ATM interface, either of the following procedures are used\:  Negotiated VPL establishment  (1) The management application creates   a VPL entry in the atmVplTable   by setting atmVplRowStatus to createAndWait(5).   This may fail for the following reasons\:   \- The selected VPI value is unavailable,   \- The selected VPI value is in use.   Otherwise, the agent creates a row and   reserves the VPI value on that port.  (2) The manager selects an existing row(s) in the   atmTrafficDescrParamTable,   thereby, selecting a set of self\-consistent   ATM traffic parameters and the service category   for receive and transmit directions of the VPL.  (2a) If no suitable row(s) in the   atmTrafficDescrParamTable exists,   the manager must create a new row(s)   in that table.  (2b) The manager characterizes the VPL's traffic   parameters through setting the   atmVplReceiveTrafficDescrIndex and the   atmVplTransmitTrafficDescrIndex values   in the VPL table, which point to the rows   containing desired ATM traffic parameter values   in the atmTrafficDescrParamTable.  The agent   will check the availability of resources and   may refuse the request.   If the transmit and receive service categories   are inconsistent, the agent should refuse the   request.  (3) The manager activates the VPL by setting the   the atmVplRowStatus to active(1).   If this set is successful, the agent has   reserved the resources to satisfy the requested   traffic parameter values and the service category   for that VPL.  (4) If the VPL terminates a VPC in the ATM host   or switch, the manager turns on the   atmVplAdminStatus to up(1) to turn the VPL   traffic flow on.  Otherwise, the   atmVpCrossConnectTable  must be used   to cross\-connect the VPL to another VPL(s)   in an ATM switch or network.  One\-Shot VPL Establishment  A VPL may also be established in one step by a set\-request with all necessary VPL parameter values and atmVplRowStatus set to createAndGo(4).  In contrast to the negotiated VPL establishment which allows for detailed error checking (i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VPL establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VPL Retirement  A VPL is released by setting atmVplRowStatus to destroy(6), and the agent may release all associated resources
        	**type**\: list of  		 :py:class:`AtmVplEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVplTable.AtmVplEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmVplTable, self).__init__()

            self.yang_name = "atmVplTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmVplEntry", ("atmvplentry", ATMMIB.AtmVplTable.AtmVplEntry))])
            self._leafs = OrderedDict()

            self.atmvplentry = YList(self)
            self._segment_path = lambda: "atmVplTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmVplTable, [], name, value)


        class AtmVplEntry(Entity):
            """
            An entry in the VPL table.  This entry is
            used to model a bi\-directional VPL.
            To create a VPL at an ATM interface,
            either of the following procedures are used\:
            
            Negotiated VPL establishment
            
            (1) The management application creates
              a VPL entry in the atmVplTable
              by setting atmVplRowStatus to createAndWait(5).
              This may fail for the following reasons\:
              \- The selected VPI value is unavailable,
              \- The selected VPI value is in use.
              Otherwise, the agent creates a row and
              reserves the VPI value on that port.
            
            (2) The manager selects an existing row(s) in the
              atmTrafficDescrParamTable,
              thereby, selecting a set of self\-consistent
              ATM traffic parameters and the service category
              for receive and transmit directions of the VPL.
            
            (2a) If no suitable row(s) in the
              atmTrafficDescrParamTable exists,
              the manager must create a new row(s)
              in that table.
            
            (2b) The manager characterizes the VPL's traffic
              parameters through setting the
              atmVplReceiveTrafficDescrIndex and the
              atmVplTransmitTrafficDescrIndex values
              in the VPL table, which point to the rows
              containing desired ATM traffic parameter values
              in the atmTrafficDescrParamTable.  The agent
              will check the availability of resources and
              may refuse the request.
              If the transmit and receive service categories
              are inconsistent, the agent should refuse the
              request.
            
            (3) The manager activates the VPL by setting the
              the atmVplRowStatus to active(1).
              If this set is successful, the agent has
              reserved the resources to satisfy the requested
              traffic parameter values and the service category
              for that VPL.
            
            (4) If the VPL terminates a VPC in the ATM host
              or switch, the manager turns on the
              atmVplAdminStatus to up(1) to turn the VPL
              traffic flow on.  Otherwise, the
              atmVpCrossConnectTable  must be used
              to cross\-connect the VPL to another VPL(s)
              in an ATM switch or network.
            
            One\-Shot VPL Establishment
            
            A VPL may also be established in one step by a
            set\-request with all necessary VPL parameter
            values and atmVplRowStatus set to createAndGo(4).
            
            In contrast to the negotiated VPL establishment
            which allows for detailed error checking
            (i.e., set errors are explicitly linked to
            particular resource acquisition failures),
            the one\-shot VPL establishment
            performs the setup on one operation but
            does not have the advantage of step\-wise
            error checking.
            
            VPL Retirement
            
            A VPL is released by setting atmVplRowStatus to
            destroy(6), and the agent may release all
            associated resources.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvplvpi  (key)
            
            	The VPI value of the VPL
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: atmvpladminstatus
            
            	This object is instanciated only for a VPL which terminates a VPC (i.e., one which is NOT cross\-connected to other VPLs). Its value specifies the desired administrative state of the VPL
            	**type**\:  :py:class:`AtmVorXAdminStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvploperstatus
            
            	The current operational status of the VPL
            	**type**\:  :py:class:`AtmVorXOperStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXOperStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvpllastchange
            
            	The value of sysUpTime at the time this VPL entered its current operational state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmvplreceivetrafficdescrindex
            
            	The value of this object identifies the row in the atmTrafficDescrParamTable which applies to the receive direction of the VPL
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvpltransmittrafficdescrindex
            
            	The value of this object identifies the row in the atmTrafficDescrParamTable which applies to the transmit direction of the VPL
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvplcrossconnectidentifier
            
            	This object is instantiated only for a VPL which is cross\-connected to other VPLs that belong to the same VPC.  All such associated VPLs have the same value of this object, and all their cross\-connections are identified either by entries that are indexed by the same value of atmVpCrossConnectIndex in the atmVpCrossConnectTable of this MIB module or by the same value of the cross\-connect index in the cross\-connect table for SVCs and Soft PVCs (defined in a separate MIB module). At no time should entries in these respective cross\-connect tables exist simultaneously with the same cross\-connect index value. The value of this object is initialized by the agent after the associated entries in the atmVpCrossConnectTable have been created
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvplrowstatus
            
            	This object is used to create, delete or modify a row in this table. To create a new VCL, this object is initially set to 'createAndWait' or 'createAndGo'.  This object should not be set to 'active' unless the following columnar objects have been set to their desired value in this row\: atmVplReceiveTrafficDescrIndex and atmVplTransmitTrafficDescrIndex. The DESCRIPTION of atmVplEntry provides further guidance to row treatment in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvplcasttype
            
            	The connection topology type
            	**type**\:  :py:class:`AtmConnCastType <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmConnCastType>`
            
            	**config**\: False
            
            .. attribute:: atmvplconnkind
            
            	The use of call control
            	**type**\:  :py:class:`AtmConnKind <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmConnKind>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmVplTable.AtmVplEntry, self).__init__()

                self.yang_name = "atmVplEntry"
                self.yang_parent_name = "atmVplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvplvpi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvplvpi', (YLeaf(YType.int32, 'atmVplVpi'), ['int'])),
                    ('atmvpladminstatus', (YLeaf(YType.enumeration, 'atmVplAdminStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXAdminStatus', '')])),
                    ('atmvploperstatus', (YLeaf(YType.enumeration, 'atmVplOperStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXOperStatus', '')])),
                    ('atmvpllastchange', (YLeaf(YType.uint32, 'atmVplLastChange'), ['int'])),
                    ('atmvplreceivetrafficdescrindex', (YLeaf(YType.int32, 'atmVplReceiveTrafficDescrIndex'), ['int'])),
                    ('atmvpltransmittrafficdescrindex', (YLeaf(YType.int32, 'atmVplTransmitTrafficDescrIndex'), ['int'])),
                    ('atmvplcrossconnectidentifier', (YLeaf(YType.int32, 'atmVplCrossConnectIdentifier'), ['int'])),
                    ('atmvplrowstatus', (YLeaf(YType.enumeration, 'atmVplRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('atmvplcasttype', (YLeaf(YType.enumeration, 'atmVplCastType'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmConnCastType', '')])),
                    ('atmvplconnkind', (YLeaf(YType.enumeration, 'atmVplConnKind'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmConnKind', '')])),
                ])
                self.ifindex = None
                self.atmvplvpi = None
                self.atmvpladminstatus = None
                self.atmvploperstatus = None
                self.atmvpllastchange = None
                self.atmvplreceivetrafficdescrindex = None
                self.atmvpltransmittrafficdescrindex = None
                self.atmvplcrossconnectidentifier = None
                self.atmvplrowstatus = None
                self.atmvplcasttype = None
                self.atmvplconnkind = None
                self._segment_path = lambda: "atmVplEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVplVpi='" + str(self.atmvplvpi) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmVplTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmVplTable.AtmVplEntry, [u'ifindex', u'atmvplvpi', u'atmvpladminstatus', u'atmvploperstatus', u'atmvpllastchange', u'atmvplreceivetrafficdescrindex', u'atmvpltransmittrafficdescrindex', u'atmvplcrossconnectidentifier', u'atmvplrowstatus', u'atmvplcasttype', u'atmvplconnkind'], name, value)




    class AtmVclTable(Entity):
        """
        The Virtual Channel Link (VCL) table.  A
        bi\-directional VCL is modeled as one entry
        in this table. This table can be used for
        PVCs, SVCs and Soft PVCs.
        
        .. attribute:: atmvclentry
        
        	An entry in the VCL table. This entry is used to model a bi\-directional VCL. To create a VCL at an ATM interface, either of the following procedures are used\:  Negotiated VCL establishment  (1) The management application creates   a VCL entry in the atmVclTable   by setting atmVclRowStatus to createAndWait(5).   This may fail for the following reasons\:   \- The selected VPI/VCI values are unavailable,   \- The selected VPI/VCI values are in use.   Otherwise, the agent creates a row and   reserves the VPI/VCI values on that port.  (2) The manager selects an existing row(s) in the   atmTrafficDescrParamTable,   thereby, selecting a set of self\-consistent   ATM traffic parameters and the service category   for receive and transmit directions of the VCL.   (2a) If no suitable row(s) in the   atmTrafficDescrParamTable exists,   the manager must create a new row(s)   in that table.  (2b) The manager characterizes the VCL's traffic   parameters through setting the   atmVclReceiveTrafficDescrIndex and the   atmVclTransmitTrafficDescrIndex values   in the VCL table, which point to the rows   containing desired ATM traffic parameter values   in the atmTrafficDescrParamTable.  The agent   will check the availability of resources and   may refuse the request.   If the transmit and receive service categories   are inconsistent, the agent should refuse the   request.  (3) The manager activates the VCL by setting the   the atmVclRowStatus to active(1) (for   requirements on this activation see the   description of atmVclRowStatus).   If this set is successful, the agent has   reserved the resources to satisfy the requested   traffic parameter values and the service category   for that VCL. (4) If the VCL terminates a VCC in the ATM host   or switch, the manager turns on the   atmVclAdminStatus to up(1) to turn the VCL   traffic flow on.  Otherwise, the   atmVcCrossConnectTable  must be used   to cross\-connect the VCL to another VCL(s)   in an ATM switch or network.  One\-Shot VCL Establishment  A VCL may also be established in one step by a set\-request with all necessary VCL parameter values and atmVclRowStatus set to createAndGo(4).  In contrast to the negotiated VCL establishment which allows for detailed error checking (i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VCL establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VCL Retirement  A VCL is released by setting atmVclRowStatus to destroy(6), and the agent may release all associated resources
        	**type**\: list of  		 :py:class:`AtmVclEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmVclTable, self).__init__()

            self.yang_name = "atmVclTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmVclEntry", ("atmvclentry", ATMMIB.AtmVclTable.AtmVclEntry))])
            self._leafs = OrderedDict()

            self.atmvclentry = YList(self)
            self._segment_path = lambda: "atmVclTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmVclTable, [], name, value)


        class AtmVclEntry(Entity):
            """
            An entry in the VCL table. This entry is
            used to model a bi\-directional VCL.
            To create a VCL at an ATM interface,
            either of the following procedures are used\:
            
            Negotiated VCL establishment
            
            (1) The management application creates
              a VCL entry in the atmVclTable
              by setting atmVclRowStatus to createAndWait(5).
              This may fail for the following reasons\:
              \- The selected VPI/VCI values are unavailable,
              \- The selected VPI/VCI values are in use.
              Otherwise, the agent creates a row and
              reserves the VPI/VCI values on that port.
            
            (2) The manager selects an existing row(s) in the
              atmTrafficDescrParamTable,
              thereby, selecting a set of self\-consistent
              ATM traffic parameters and the service category
              for receive and transmit directions of the VCL.
            
            
            (2a) If no suitable row(s) in the
              atmTrafficDescrParamTable exists,
              the manager must create a new row(s)
              in that table.
            
            (2b) The manager characterizes the VCL's traffic
              parameters through setting the
              atmVclReceiveTrafficDescrIndex and the
              atmVclTransmitTrafficDescrIndex values
              in the VCL table, which point to the rows
              containing desired ATM traffic parameter values
              in the atmTrafficDescrParamTable.  The agent
              will check the availability of resources and
              may refuse the request.
              If the transmit and receive service categories
              are inconsistent, the agent should refuse the
              request.
            
            (3) The manager activates the VCL by setting the
              the atmVclRowStatus to active(1) (for
              requirements on this activation see the
              description of atmVclRowStatus).
              If this set is successful, the agent has
              reserved the resources to satisfy the requested
              traffic parameter values and the service category
              for that VCL.
            (4) If the VCL terminates a VCC in the ATM host
              or switch, the manager turns on the
              atmVclAdminStatus to up(1) to turn the VCL
              traffic flow on.  Otherwise, the
              atmVcCrossConnectTable  must be used
              to cross\-connect the VCL to another VCL(s)
              in an ATM switch or network.
            
            One\-Shot VCL Establishment
            
            A VCL may also be established in one step by a
            set\-request with all necessary VCL parameter
            values and atmVclRowStatus set to createAndGo(4).
            
            In contrast to the negotiated VCL establishment
            which allows for detailed error checking
            (i.e., set errors are explicitly linked to
            particular resource acquisition failures),
            the one\-shot VCL establishment
            performs the setup on one operation but
            does not have the advantage of step\-wise
            error checking.
            
            VCL Retirement
            
            A VCL is released by setting atmVclRowStatus to
            destroy(6), and the agent may release all
            associated resources.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvclvpi  (key)
            
            	The VPI value of the VCL
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: atmvclvci  (key)
            
            	The VCI value of the VCL
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: atmvcladminstatus
            
            	This object is instanciated only for a VCL which terminates a VCC (i.e., one which is NOT cross\-connected to other VCLs). Its value specifies the desired administrative state of the VCL
            	**type**\:  :py:class:`AtmVorXAdminStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvcloperstatus
            
            	The current operational status of the VCL
            	**type**\:  :py:class:`AtmVorXOperStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXOperStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvcllastchange
            
            	The value of sysUpTime at the time this VCL entered its current operational state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmvclreceivetrafficdescrindex
            
            	The value of this object identifies the row in the ATM Traffic Descriptor Table which applies to the receive direction of this VCL
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvcltransmittrafficdescrindex
            
            	The value of this object identifies the row of the ATM Traffic Descriptor Table which applies to the transmit direction of this VCL
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvccaaltype
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL is in use. The type of AAL used on this VCC. The AAL type includes AAL1, AAL2, AAL3/4, and AAL5. The other(4) may be user\-defined AAL type.  The unknown type indicates that the AAL type cannot be determined
            	**type**\:  :py:class:`AtmVccAalType <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry.AtmVccAalType>`
            
            	**config**\: False
            
            .. attribute:: atmvccaal5cpcstransmitsdusize
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL5 is in use. The maximum AAL5 CPCS SDU size in octets that is supported on the transmit direction of this VCC
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: atmvccaal5cpcsreceivesdusize
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL5 is in use. The maximum AAL5 CPCS SDU size in octets that is supported on the receive direction of this VCC
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: atmvccaal5encapstype
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL5 is in use. The type of data encapsulation used over the AAL5 SSCS layer. The definitions reference RFC 1483 Multiprotocol Encapsulation over ATM AAL5 and to the ATM Forum LAN Emulation specification
            	**type**\:  :py:class:`AtmVccAal5EncapsType <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry.AtmVccAal5EncapsType>`
            
            	**config**\: False
            
            .. attribute:: atmvclcrossconnectidentifier
            
            	This object is instantiated only for a VCL which is cross\-connected to other VCLs that belong to the same VCC.  All such associated VCLs have the same value of this object, and all their cross\-connections are identified either by entries that are indexed by the same value of atmVcCrossConnectIndex in the atmVcCrossConnectTable of this MIB module or by the same value of the cross\-connect index in the cross\-connect table for SVCs and Soft PVCs (defined in a separate MIB module).  At no time should entries in these respective cross\-connect tables exist simultaneously with the same cross\-connect index value. The value of this object is initialized by the agent after the associated entries in the atmVcCrossConnectTable have been created
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvclrowstatus
            
            	This object is used to create, delete or modify a row in this table.  To create a new VCL, this object is initially set to 'createAndWait' or 'createAndGo'. This object should not be set to 'active' unless the following columnar objects have been set to their desired value in this row\: atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex. In addition, if the local VCL end\-point is also the VCC end\-point\: atmVccAalType. In addition, for AAL5 connections only\: atmVccAal5CpcsTransmitSduSize, atmVccAal5CpcsReceiveSduSize, and atmVccAal5EncapsType. (The existence of these objects imply the AAL connection type.). The DESCRIPTION of atmVclEntry provides further guidance to row treatment in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvclcasttype
            
            	The connection topology type
            	**type**\:  :py:class:`AtmConnCastType <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmConnCastType>`
            
            	**config**\: False
            
            .. attribute:: atmvclconnkind
            
            	The use of call control
            	**type**\:  :py:class:`AtmConnKind <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmConnKind>`
            
            	**config**\: False
            
            .. attribute:: catmxvcloamloopbackfreq
            
            	Specifies OAM loopback frequency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloamretryfreq
            
            	Specifies OAM retry polling frequency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloamupretrycount
            
            	Specifies OAM retry count before declaring a VC  is up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmxvcloamdownretrycount
            
            	Specifies OAM retry count before declaring a VC  is down
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmxvcloamendccactcount
            
            	Specifies OAM End\-to\-end Continuity check (CC)  Activation retry count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmxvcloamendccdeactcount
            
            	Specifies OAM End\-to\-end Continuity check (CC)  Deactivation retry count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmxvcloamendccretryfreq
            
            	Specifies OAM End\-to\-end Continuity check (CC)  Activation/Deactivation retry frequency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloamsegccactcount
            
            	Specifies OAM Segment Continuity check (CC)  Activation retry count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmxvcloamsegccdeactcount
            
            	Specifies OAM Segment Continuity check (CC)  Deactivation retry count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: catmxvcloamsegccretryfreq
            
            	Specifies OAM Segment Continuity check (CC)  Activation/Deactivation retry frequency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloammanage
            
            	Specifies OAM Enable/Disable on the VC. true(1) indicates that OAM is enabled on the VC. false(2) indicates that OAM is disabled on the VC
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: catmxvcloamloopbkstatus
            
            	Indicates OAM loopback status of the VC. disabled(1)  \-\-   No OAMs on this VC. sent(2)      \-\-   OAM sent, waiting for echo. received(3)  \-\-   OAM received from target. failed(4)    \-\-   Last OAM did not return
            	**type**\:  :py:class:`CatmxVclOamLoopBkStatus <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry.CatmxVclOamLoopBkStatus>`
            
            	**config**\: False
            
            .. attribute:: catmxvcloamvcstate
            
            	Indicates the state of VC OAM. downRetry(1)   \-\-  Loopback failed. Retry sending                     loopbacks with retry frequency.                     VC is up. verified(2)    \-\-  Loopback is successful. notVerified(3) \-\-  Not verified by loopback,                     AIS/RDI conditions are cleared. upRetry(4)     \-\-  Retry successive loopbacks.                     VC is down. aisRDI(5)      \-\-  Received AIS/RDI. Loopback are                     not sent in this state. aisOut(6)      \-\-  Sending AIS. Loopback and reply are                     not sent in this state. notManaged(7)  \-\-  VC is not managed by OAM
            	**type**\:  :py:class:`CatmxVclOamVcState <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry.CatmxVclOamVcState>`
            
            	**config**\: False
            
            .. attribute:: catmxvcloamendccstatus
            
            	Indicates OAM End\-to\-end Continuity check (CC)  status
            	**type**\:  :py:class:`OamCCStatus <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamCCStatus>`
            
            	**config**\: False
            
            .. attribute:: catmxvcloamsegccstatus
            
            	Indicates OAM Segment Continuity check (CC) status
            	**type**\:  :py:class:`OamCCStatus <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamCCStatus>`
            
            	**config**\: False
            
            .. attribute:: catmxvcloamendccvcstate
            
            	Indicates OAM End\-to\-end Continuity check (CC)  VC state
            	**type**\:  :py:class:`OamCCVcState <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamCCVcState>`
            
            	**config**\: False
            
            .. attribute:: catmxvcloamsegccvcstate
            
            	Indicates OAM Segment Continuity check (CC) VC  state
            	**type**\:  :py:class:`OamCCVcState <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamCCVcState>`
            
            	**config**\: False
            
            .. attribute:: catmxvcloamcellsreceived
            
            	Indicates the number of OAM cells received on  this VC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamcellssent
            
            	Indicates the number of OAM cells sent on  this VC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamcellsdropped
            
            	Indicates the number of OAM cells dropped on  this VC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: cells
            
            .. attribute:: catmxvcloaminf5ais
            
            	Indicates the number of received OAM  F5 Alarm Indication Signal (AIS) cells from the VC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamoutf5ais
            
            	Indicates the number of transmitted OAM  F5 Alarm Indication Signal (AIS) cells to the VC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: cells
            
            .. attribute:: catmxvcloaminf5rdi
            
            	Indicates the number of received OAM  F5 Remote Detection Indication (RDI) cells from  the VC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamoutf5rdi
            
            	Indicates the number of transmitted OAM  F5 Remote Detection Indication (RDI) cells to the VC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: cells
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmVclTable.AtmVclEntry, self).__init__()

                self.yang_name = "atmVclEntry"
                self.yang_parent_name = "atmVclTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.int32, 'atmVclVpi'), ['int'])),
                    ('atmvclvci', (YLeaf(YType.int32, 'atmVclVci'), ['int'])),
                    ('atmvcladminstatus', (YLeaf(YType.enumeration, 'atmVclAdminStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXAdminStatus', '')])),
                    ('atmvcloperstatus', (YLeaf(YType.enumeration, 'atmVclOperStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXOperStatus', '')])),
                    ('atmvcllastchange', (YLeaf(YType.uint32, 'atmVclLastChange'), ['int'])),
                    ('atmvclreceivetrafficdescrindex', (YLeaf(YType.int32, 'atmVclReceiveTrafficDescrIndex'), ['int'])),
                    ('atmvcltransmittrafficdescrindex', (YLeaf(YType.int32, 'atmVclTransmitTrafficDescrIndex'), ['int'])),
                    ('atmvccaaltype', (YLeaf(YType.enumeration, 'atmVccAalType'), [('ydk.models.cisco_ios_xe.ATM_MIB', 'ATMMIB', 'AtmVclTable.AtmVclEntry.AtmVccAalType')])),
                    ('atmvccaal5cpcstransmitsdusize', (YLeaf(YType.int32, 'atmVccAal5CpcsTransmitSduSize'), ['int'])),
                    ('atmvccaal5cpcsreceivesdusize', (YLeaf(YType.int32, 'atmVccAal5CpcsReceiveSduSize'), ['int'])),
                    ('atmvccaal5encapstype', (YLeaf(YType.enumeration, 'atmVccAal5EncapsType'), [('ydk.models.cisco_ios_xe.ATM_MIB', 'ATMMIB', 'AtmVclTable.AtmVclEntry.AtmVccAal5EncapsType')])),
                    ('atmvclcrossconnectidentifier', (YLeaf(YType.int32, 'atmVclCrossConnectIdentifier'), ['int'])),
                    ('atmvclrowstatus', (YLeaf(YType.enumeration, 'atmVclRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('atmvclcasttype', (YLeaf(YType.enumeration, 'atmVclCastType'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmConnCastType', '')])),
                    ('atmvclconnkind', (YLeaf(YType.enumeration, 'atmVclConnKind'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmConnKind', '')])),
                    ('catmxvcloamloopbackfreq', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamLoopbackFreq'), ['int'])),
                    ('catmxvcloamretryfreq', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamRetryFreq'), ['int'])),
                    ('catmxvcloamupretrycount', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamUpRetryCount'), ['int'])),
                    ('catmxvcloamdownretrycount', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamDownRetryCount'), ['int'])),
                    ('catmxvcloamendccactcount', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamEndCCActCount'), ['int'])),
                    ('catmxvcloamendccdeactcount', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamEndCCDeActCount'), ['int'])),
                    ('catmxvcloamendccretryfreq', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamEndCCRetryFreq'), ['int'])),
                    ('catmxvcloamsegccactcount', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamSegCCActCount'), ['int'])),
                    ('catmxvcloamsegccdeactcount', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamSegCCDeActCount'), ['int'])),
                    ('catmxvcloamsegccretryfreq', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamSegCCRetryFreq'), ['int'])),
                    ('catmxvcloammanage', (YLeaf(YType.boolean, 'CISCO-ATM-EXT-MIB:catmxVclOamManage'), ['bool'])),
                    ('catmxvcloamloopbkstatus', (YLeaf(YType.enumeration, 'CISCO-ATM-EXT-MIB:catmxVclOamLoopBkStatus'), [('ydk.models.cisco_ios_xe.ATM_MIB', 'ATMMIB', 'AtmVclTable.AtmVclEntry.CatmxVclOamLoopBkStatus')])),
                    ('catmxvcloamvcstate', (YLeaf(YType.enumeration, 'CISCO-ATM-EXT-MIB:catmxVclOamVcState'), [('ydk.models.cisco_ios_xe.ATM_MIB', 'ATMMIB', 'AtmVclTable.AtmVclEntry.CatmxVclOamVcState')])),
                    ('catmxvcloamendccstatus', (YLeaf(YType.enumeration, 'CISCO-ATM-EXT-MIB:catmxVclOamEndCCStatus'), [('ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB', 'OamCCStatus', '')])),
                    ('catmxvcloamsegccstatus', (YLeaf(YType.enumeration, 'CISCO-ATM-EXT-MIB:catmxVclOamSegCCStatus'), [('ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB', 'OamCCStatus', '')])),
                    ('catmxvcloamendccvcstate', (YLeaf(YType.enumeration, 'CISCO-ATM-EXT-MIB:catmxVclOamEndCCVcState'), [('ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB', 'OamCCVcState', '')])),
                    ('catmxvcloamsegccvcstate', (YLeaf(YType.enumeration, 'CISCO-ATM-EXT-MIB:catmxVclOamSegCCVcState'), [('ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB', 'OamCCVcState', '')])),
                    ('catmxvcloamcellsreceived', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamCellsReceived'), ['int'])),
                    ('catmxvcloamcellssent', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamCellsSent'), ['int'])),
                    ('catmxvcloamcellsdropped', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamCellsDropped'), ['int'])),
                    ('catmxvcloaminf5ais', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamInF5ais'), ['int'])),
                    ('catmxvcloamoutf5ais', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamOutF5ais'), ['int'])),
                    ('catmxvcloaminf5rdi', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamInF5rdi'), ['int'])),
                    ('catmxvcloamoutf5rdi', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:catmxVclOamOutF5rdi'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.atmvcladminstatus = None
                self.atmvcloperstatus = None
                self.atmvcllastchange = None
                self.atmvclreceivetrafficdescrindex = None
                self.atmvcltransmittrafficdescrindex = None
                self.atmvccaaltype = None
                self.atmvccaal5cpcstransmitsdusize = None
                self.atmvccaal5cpcsreceivesdusize = None
                self.atmvccaal5encapstype = None
                self.atmvclcrossconnectidentifier = None
                self.atmvclrowstatus = None
                self.atmvclcasttype = None
                self.atmvclconnkind = None
                self.catmxvcloamloopbackfreq = None
                self.catmxvcloamretryfreq = None
                self.catmxvcloamupretrycount = None
                self.catmxvcloamdownretrycount = None
                self.catmxvcloamendccactcount = None
                self.catmxvcloamendccdeactcount = None
                self.catmxvcloamendccretryfreq = None
                self.catmxvcloamsegccactcount = None
                self.catmxvcloamsegccdeactcount = None
                self.catmxvcloamsegccretryfreq = None
                self.catmxvcloammanage = None
                self.catmxvcloamloopbkstatus = None
                self.catmxvcloamvcstate = None
                self.catmxvcloamendccstatus = None
                self.catmxvcloamsegccstatus = None
                self.catmxvcloamendccvcstate = None
                self.catmxvcloamsegccvcstate = None
                self.catmxvcloamcellsreceived = None
                self.catmxvcloamcellssent = None
                self.catmxvcloamcellsdropped = None
                self.catmxvcloaminf5ais = None
                self.catmxvcloamoutf5ais = None
                self.catmxvcloaminf5rdi = None
                self.catmxvcloamoutf5rdi = None
                self._segment_path = lambda: "atmVclEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmVclTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmVclTable.AtmVclEntry, [u'ifindex', u'atmvclvpi', u'atmvclvci', u'atmvcladminstatus', u'atmvcloperstatus', u'atmvcllastchange', u'atmvclreceivetrafficdescrindex', u'atmvcltransmittrafficdescrindex', u'atmvccaaltype', u'atmvccaal5cpcstransmitsdusize', u'atmvccaal5cpcsreceivesdusize', u'atmvccaal5encapstype', u'atmvclcrossconnectidentifier', u'atmvclrowstatus', u'atmvclcasttype', u'atmvclconnkind', 'catmxvcloamloopbackfreq', 'catmxvcloamretryfreq', 'catmxvcloamupretrycount', 'catmxvcloamdownretrycount', 'catmxvcloamendccactcount', 'catmxvcloamendccdeactcount', 'catmxvcloamendccretryfreq', 'catmxvcloamsegccactcount', 'catmxvcloamsegccdeactcount', 'catmxvcloamsegccretryfreq', 'catmxvcloammanage', 'catmxvcloamloopbkstatus', 'catmxvcloamvcstate', 'catmxvcloamendccstatus', 'catmxvcloamsegccstatus', 'catmxvcloamendccvcstate', 'catmxvcloamsegccvcstate', 'catmxvcloamcellsreceived', 'catmxvcloamcellssent', 'catmxvcloamcellsdropped', 'catmxvcloaminf5ais', 'catmxvcloamoutf5ais', 'catmxvcloaminf5rdi', 'catmxvcloamoutf5rdi'], name, value)

            class AtmVccAal5EncapsType(Enum):
                """
                AtmVccAal5EncapsType (Enum Class)

                An instance of this object only exists when the

                local VCL end\-point is also the VCC end\-point,

                and AAL5 is in use.

                The type of data encapsulation used over

                the AAL5 SSCS layer. The definitions reference

                RFC 1483 Multiprotocol Encapsulation

                over ATM AAL5 and to the ATM Forum

                LAN Emulation specification.

                .. data:: vcMultiplexRoutedProtocol = 1

                .. data:: vcMultiplexBridgedProtocol8023 = 2

                .. data:: vcMultiplexBridgedProtocol8025 = 3

                .. data:: vcMultiplexBridgedProtocol8026 = 4

                .. data:: vcMultiplexLANemulation8023 = 5

                .. data:: vcMultiplexLANemulation8025 = 6

                .. data:: llcEncapsulation = 7

                .. data:: multiprotocolFrameRelaySscs = 8

                .. data:: other = 9

                .. data:: unknown = 10

                """

                vcMultiplexRoutedProtocol = Enum.YLeaf(1, "vcMultiplexRoutedProtocol")

                vcMultiplexBridgedProtocol8023 = Enum.YLeaf(2, "vcMultiplexBridgedProtocol8023")

                vcMultiplexBridgedProtocol8025 = Enum.YLeaf(3, "vcMultiplexBridgedProtocol8025")

                vcMultiplexBridgedProtocol8026 = Enum.YLeaf(4, "vcMultiplexBridgedProtocol8026")

                vcMultiplexLANemulation8023 = Enum.YLeaf(5, "vcMultiplexLANemulation8023")

                vcMultiplexLANemulation8025 = Enum.YLeaf(6, "vcMultiplexLANemulation8025")

                llcEncapsulation = Enum.YLeaf(7, "llcEncapsulation")

                multiprotocolFrameRelaySscs = Enum.YLeaf(8, "multiprotocolFrameRelaySscs")

                other = Enum.YLeaf(9, "other")

                unknown = Enum.YLeaf(10, "unknown")


            class AtmVccAalType(Enum):
                """
                AtmVccAalType (Enum Class)

                An instance of this object only exists when the

                local VCL end\-point is also the VCC end\-point,

                and AAL is in use.

                The type of AAL used on this VCC.

                The AAL type includes AAL1, AAL2, AAL3/4,

                and AAL5. The other(4) may be user\-defined

                AAL type.  The unknown type indicates that

                the AAL type cannot be determined.

                .. data:: aal1 = 1

                .. data:: aal34 = 2

                .. data:: aal5 = 3

                .. data:: other = 4

                .. data:: unknown = 5

                .. data:: aal2 = 6

                """

                aal1 = Enum.YLeaf(1, "aal1")

                aal34 = Enum.YLeaf(2, "aal34")

                aal5 = Enum.YLeaf(3, "aal5")

                other = Enum.YLeaf(4, "other")

                unknown = Enum.YLeaf(5, "unknown")

                aal2 = Enum.YLeaf(6, "aal2")


            class CatmxVclOamLoopBkStatus(Enum):
                """
                CatmxVclOamLoopBkStatus (Enum Class)

                Indicates OAM loopback status of the VC.

                disabled(1)  \-\-   No OAMs on this VC.

                sent(2)      \-\-   OAM sent, waiting for echo.

                received(3)  \-\-   OAM received from target.

                failed(4)    \-\-   Last OAM did not return.

                .. data:: disabled = 1

                .. data:: sent = 2

                .. data:: received = 3

                .. data:: failed = 4

                """

                disabled = Enum.YLeaf(1, "disabled")

                sent = Enum.YLeaf(2, "sent")

                received = Enum.YLeaf(3, "received")

                failed = Enum.YLeaf(4, "failed")


            class CatmxVclOamVcState(Enum):
                """
                CatmxVclOamVcState (Enum Class)

                Indicates the state of VC OAM.

                downRetry(1)   \-\-  Loopback failed. Retry sending 

                                   loopbacks with retry frequency. 

                                   VC is up.

                verified(2)    \-\-  Loopback is successful.

                notVerified(3) \-\-  Not verified by loopback, 

                                   AIS/RDI conditions are cleared.

                upRetry(4)     \-\-  Retry successive loopbacks. 

                                   VC is down.

                aisRDI(5)      \-\-  Received AIS/RDI. Loopback are 

                                   not sent in this state.

                aisOut(6)      \-\-  Sending AIS. Loopback and reply are 

                                   not sent in this state.

                notManaged(7)  \-\-  VC is not managed by OAM.

                .. data:: downRetry = 1

                .. data:: verified = 2

                .. data:: notVerified = 3

                .. data:: upRetry = 4

                .. data:: aisRDI = 5

                .. data:: aisOut = 6

                .. data:: notManaged = 7

                """

                downRetry = Enum.YLeaf(1, "downRetry")

                verified = Enum.YLeaf(2, "verified")

                notVerified = Enum.YLeaf(3, "notVerified")

                upRetry = Enum.YLeaf(4, "upRetry")

                aisRDI = Enum.YLeaf(5, "aisRDI")

                aisOut = Enum.YLeaf(6, "aisOut")

                notManaged = Enum.YLeaf(7, "notManaged")





    class AtmVpCrossConnectTable(Entity):
        """
        The ATM VP Cross Connect table for PVCs.
        An entry in this table models two
        cross\-connected VPLs.
        Each VPL must have its atmConnKind set
        to pvc(1).
        
        .. attribute:: atmvpcrossconnectentry
        
        	An entry in the ATM VP Cross Connect table. This entry is used to model a bi\-directional ATM VP cross\-connect which cross\-connects two VPLs.  Step\-wise Procedures to set up a VP Cross\-connect  Once the entries in the atmVplTable are created, the following procedures are used to cross\-connect the VPLs together.  (1) The manager obtains a unique    atmVpCrossConnectIndex by reading the    atmVpCrossConnectIndexNext object.  (2) Next, the manager creates a set of one    or more rows in the ATM VP Cross Connect    Table, one for each cross\-connection between    two VPLs.  Each row is indexed by the ATM    interface port numbers and VPI values of the    two ends of that cross\-connection.    This set of rows specifies the topology of the    VPC cross\-connect and is identified by a single    value of atmVpCrossConnectIndex.  Negotiated VP Cross\-Connect Establishment  (2a) The manager creates a row in this table by    setting atmVpCrossConnectRowStatus to    createAndWait(5).  The agent checks the    requested topology and the mutual sanity of    the ATM traffic parameters and    service categories, i.e., the row creation    fails if\:    \- the requested topology is incompatible with      associated values of atmVplCastType,    \- the requested topology is not supported      by the agent,    \- the traffic/service category parameter values      associated with the requested row are      incompatible with those of already existing      rows for this VP cross\-connect.    [For example, for setting up    a point\-to\-point VP cross\-connect, the    ATM traffic parameters in the receive direction    of a VPL at the low end of the cross\-connect    must equal to the traffic parameters in the    transmit direction of the other VPL at the    high end of the cross\-connect,    otherwise, the row creation fails.]    The agent also checks for internal errors    in building the cross\-connect.     The atmVpCrossConnectIndex values in the    corresponding atmVplTable rows are filled    in by the agent at this point.  (2b) The manager promotes the row in the    atmVpCrossConnectTable by setting    atmVpCrossConnectRowStatus to active(1).  If    this set is successful, the agent has reserved    the resources specified by the ATM traffic    parameter and Service category values    for each direction of the VP cross\-connect    in an ATM switch or network.  (3) The manager sets the    atmVpCrossConnectAdminStatus to up(1) in all    rows of this VP cross\-connect to turn the    traffic flow on.   One\-Shot VP Cross\-Connect Establishment  A VP cross\-connect may also be established in one step by a set\-request with all necessary parameter values and atmVpCrossConnectRowStatus set to createAndGo(4).  In contrast to the negotiated VP cross\-connect establishment which allows for detailed error checking (i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VP cross\-connect establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VP Cross\-Connect Retirement  A VP cross\-connect identified by a particular value of atmVpCrossConnectIndex is released by\:  (1) Setting atmVpCrossConnectRowStatus of all    rows identified by this value of    atmVpCrossConnectIndex to destroy(6).    The agent may release all    associated resources, and the    atmVpCrossConnectIndex values in the    corresponding atmVplTable row are removed.    Note that a situation when only a subset of    the associated rows are deleted corresponds    to a VP topology change.  (2) After deletion of the appropriate    atmVpCrossConnectEntries, the manager may    set atmVplRowStatus to destroy(6) the    associated VPLs.  The agent releases    the resources and removes the associated    rows in the atmVplTable.  VP Cross\-connect Reconfiguration  At the discretion of the agent, a VP cross\-connect may be reconfigured by adding and/or deleting leafs to/from the VP topology as per the VP cross\-connect establishment/retirement procedures. Reconfiguration of traffic/service category parameter values requires release of the VP cross\-connect before those parameter values may by changed for individual VPLs
        	**type**\: list of  		 :py:class:`AtmVpCrossConnectEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmVpCrossConnectTable, self).__init__()

            self.yang_name = "atmVpCrossConnectTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmVpCrossConnectEntry", ("atmvpcrossconnectentry", ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry))])
            self._leafs = OrderedDict()

            self.atmvpcrossconnectentry = YList(self)
            self._segment_path = lambda: "atmVpCrossConnectTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmVpCrossConnectTable, [], name, value)


        class AtmVpCrossConnectEntry(Entity):
            """
            An entry in the ATM VP Cross Connect table.
            This entry is used to model a bi\-directional
            ATM VP cross\-connect which cross\-connects
            two VPLs.
            
            Step\-wise Procedures to set up a VP Cross\-connect
            
            Once the entries in the atmVplTable are created,
            the following procedures are used
            to cross\-connect the VPLs together.
            
            (1) The manager obtains a unique
               atmVpCrossConnectIndex by reading the
               atmVpCrossConnectIndexNext object.
            
            (2) Next, the manager creates a set of one
               or more rows in the ATM VP Cross Connect
               Table, one for each cross\-connection between
               two VPLs.  Each row is indexed by the ATM
               interface port numbers and VPI values of the
               two ends of that cross\-connection.
               This set of rows specifies the topology of the
               VPC cross\-connect and is identified by a single
               value of atmVpCrossConnectIndex.
            
            Negotiated VP Cross\-Connect Establishment
            
            (2a) The manager creates a row in this table by
               setting atmVpCrossConnectRowStatus to
               createAndWait(5).  The agent checks the
               requested topology and the mutual sanity of
               the ATM traffic parameters and
               service categories, i.e., the row creation
               fails if\:
               \- the requested topology is incompatible with
                 associated values of atmVplCastType,
               \- the requested topology is not supported
                 by the agent,
               \- the traffic/service category parameter values
                 associated with the requested row are
                 incompatible with those of already existing
                 rows for this VP cross\-connect.
               [For example, for setting up
               a point\-to\-point VP cross\-connect, the
               ATM traffic parameters in the receive direction
               of a VPL at the low end of the cross\-connect
               must equal to the traffic parameters in the
               transmit direction of the other VPL at the
               high end of the cross\-connect,
               otherwise, the row creation fails.]
               The agent also checks for internal errors
               in building the cross\-connect.
            
               The atmVpCrossConnectIndex values in the
               corresponding atmVplTable rows are filled
               in by the agent at this point.
            
            (2b) The manager promotes the row in the
               atmVpCrossConnectTable by setting
               atmVpCrossConnectRowStatus to active(1).  If
               this set is successful, the agent has reserved
               the resources specified by the ATM traffic
               parameter and Service category values
               for each direction of the VP cross\-connect
               in an ATM switch or network.
            
            (3) The manager sets the
               atmVpCrossConnectAdminStatus to up(1) in all
               rows of this VP cross\-connect to turn the
               traffic flow on.
            
            
            One\-Shot VP Cross\-Connect Establishment
            
            A VP cross\-connect may also be established in
            one step by a set\-request with all necessary
            parameter values and atmVpCrossConnectRowStatus
            set to createAndGo(4).
            
            In contrast to the negotiated VP cross\-connect
            establishment which allows for detailed error
            checking (i.e., set errors are explicitly linked
            to particular resource acquisition failures),
            the one\-shot VP cross\-connect establishment
            performs the setup on one operation but does not
            have the advantage of step\-wise error checking.
            
            VP Cross\-Connect Retirement
            
            A VP cross\-connect identified by a particular
            value of atmVpCrossConnectIndex is released by\:
            
            (1) Setting atmVpCrossConnectRowStatus of all
               rows identified by this value of
               atmVpCrossConnectIndex to destroy(6).
               The agent may release all
               associated resources, and the
               atmVpCrossConnectIndex values in the
               corresponding atmVplTable row are removed.
               Note that a situation when only a subset of
               the associated rows are deleted corresponds
               to a VP topology change.
            
            (2) After deletion of the appropriate
               atmVpCrossConnectEntries, the manager may
               set atmVplRowStatus to destroy(6) the
               associated VPLs.  The agent releases
               the resources and removes the associated
               rows in the atmVplTable.
            
            VP Cross\-connect Reconfiguration
            
            At the discretion of the agent, a VP
            cross\-connect may be reconfigured by
            adding and/or deleting leafs to/from
            the VP topology as per the VP cross\-connect
            establishment/retirement procedures.
            Reconfiguration of traffic/service category parameter
            values requires release of the VP cross\-connect
            before those parameter values may by changed
            for individual VPLs.
            
            .. attribute:: atmvpcrossconnectindex  (key)
            
            	A unique value to identify this VP cross\-connect. For each VPL associated with this cross\-connect, the agent reports this cross\-connect index value in the atmVplCrossConnectIdentifier attribute of the corresponding atmVplTable entries
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnectlowifindex  (key)
            
            	The ifIndex value of the ATM interface for this VP cross\-connect. The term low implies that this ATM interface has the numerically lower ifIndex value than the other ATM interface identified in the same atmVpCrossConnectEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnectlowvpi  (key)
            
            	The VPI value at the ATM interface associated with the VP cross\-connect that is identified by atmVpCrossConnectLowIfIndex
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnecthighifindex  (key)
            
            	The ifIndex value of the ATM interface for this VP cross\-connect. The term high implies that this ATM interface has the numerically higher ifIndex value than the  other ATM interface identified in the same atmVpCrossConnectEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnecthighvpi  (key)
            
            	The VPI value at the ATM interface associated with the VP cross\-connect that is identified by atmVpCrossConnectHighIfIndex
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnectadminstatus
            
            	The desired administrative status of this bi\-directional VP cross\-connect
            	**type**\:  :py:class:`AtmVorXAdminStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnectl2hoperstatus
            
            	The operational status of the VP cross\-connect in one direction; (i.e., from the low to high direction)
            	**type**\:  :py:class:`AtmVorXOperStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXOperStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnecth2loperstatus
            
            	The operational status of the VP cross\-connect in one direction; (i.e., from the high to low direction)
            	**type**\:  :py:class:`AtmVorXOperStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXOperStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnectl2hlastchange
            
            	The value of sysUpTime at the time this VP cross\-connect entered its current operational state in the low to high direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnecth2llastchange
            
            	The value of sysUpTime at the time this VP cross\-connect entered its current operational in the high to low direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmvpcrossconnectrowstatus
            
            	The status of this entry in the atmVpCrossConnectTable.  This object is used to create a cross\-connect for cross\-connecting VPLs which are created using the atmVplTable or to change or delete an existing cross\-connect. This object must be initially set to `createAndWait' or 'createAndGo'. To turn on a VP cross\-connect, the atmVpCrossConnectAdminStatus is set to `up'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry, self).__init__()

                self.yang_name = "atmVpCrossConnectEntry"
                self.yang_parent_name = "atmVpCrossConnectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['atmvpcrossconnectindex','atmvpcrossconnectlowifindex','atmvpcrossconnectlowvpi','atmvpcrossconnecthighifindex','atmvpcrossconnecthighvpi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('atmvpcrossconnectindex', (YLeaf(YType.int32, 'atmVpCrossConnectIndex'), ['int'])),
                    ('atmvpcrossconnectlowifindex', (YLeaf(YType.int32, 'atmVpCrossConnectLowIfIndex'), ['int'])),
                    ('atmvpcrossconnectlowvpi', (YLeaf(YType.int32, 'atmVpCrossConnectLowVpi'), ['int'])),
                    ('atmvpcrossconnecthighifindex', (YLeaf(YType.int32, 'atmVpCrossConnectHighIfIndex'), ['int'])),
                    ('atmvpcrossconnecthighvpi', (YLeaf(YType.int32, 'atmVpCrossConnectHighVpi'), ['int'])),
                    ('atmvpcrossconnectadminstatus', (YLeaf(YType.enumeration, 'atmVpCrossConnectAdminStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXAdminStatus', '')])),
                    ('atmvpcrossconnectl2hoperstatus', (YLeaf(YType.enumeration, 'atmVpCrossConnectL2HOperStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXOperStatus', '')])),
                    ('atmvpcrossconnecth2loperstatus', (YLeaf(YType.enumeration, 'atmVpCrossConnectH2LOperStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXOperStatus', '')])),
                    ('atmvpcrossconnectl2hlastchange', (YLeaf(YType.uint32, 'atmVpCrossConnectL2HLastChange'), ['int'])),
                    ('atmvpcrossconnecth2llastchange', (YLeaf(YType.uint32, 'atmVpCrossConnectH2LLastChange'), ['int'])),
                    ('atmvpcrossconnectrowstatus', (YLeaf(YType.enumeration, 'atmVpCrossConnectRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.atmvpcrossconnectindex = None
                self.atmvpcrossconnectlowifindex = None
                self.atmvpcrossconnectlowvpi = None
                self.atmvpcrossconnecthighifindex = None
                self.atmvpcrossconnecthighvpi = None
                self.atmvpcrossconnectadminstatus = None
                self.atmvpcrossconnectl2hoperstatus = None
                self.atmvpcrossconnecth2loperstatus = None
                self.atmvpcrossconnectl2hlastchange = None
                self.atmvpcrossconnecth2llastchange = None
                self.atmvpcrossconnectrowstatus = None
                self._segment_path = lambda: "atmVpCrossConnectEntry" + "[atmVpCrossConnectIndex='" + str(self.atmvpcrossconnectindex) + "']" + "[atmVpCrossConnectLowIfIndex='" + str(self.atmvpcrossconnectlowifindex) + "']" + "[atmVpCrossConnectLowVpi='" + str(self.atmvpcrossconnectlowvpi) + "']" + "[atmVpCrossConnectHighIfIndex='" + str(self.atmvpcrossconnecthighifindex) + "']" + "[atmVpCrossConnectHighVpi='" + str(self.atmvpcrossconnecthighvpi) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmVpCrossConnectTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry, [u'atmvpcrossconnectindex', u'atmvpcrossconnectlowifindex', u'atmvpcrossconnectlowvpi', u'atmvpcrossconnecthighifindex', u'atmvpcrossconnecthighvpi', u'atmvpcrossconnectadminstatus', u'atmvpcrossconnectl2hoperstatus', u'atmvpcrossconnecth2loperstatus', u'atmvpcrossconnectl2hlastchange', u'atmvpcrossconnecth2llastchange', u'atmvpcrossconnectrowstatus'], name, value)




    class AtmVcCrossConnectTable(Entity):
        """
        The ATM VC Cross Connect table for PVCs.
        An entry in this table models two
        cross\-connected VCLs.
        Each VCL must have its atmConnKind set
        to pvc(1).
        
        .. attribute:: atmvccrossconnectentry
        
        	An entry in the ATM VC Cross Connect table. This entry is used to model a bi\-directional ATM VC cross\-connect cross\-connecting two end points.  Step\-wise Procedures to set up a VC Cross\-connect  Once the entries in the atmVclTable are created, the following procedures are used to cross\-connect the VCLs together to form a VCC segment.  (1) The manager obtains a unique    atmVcCrossConnectIndex by reading the    atmVcCrossConnectIndexNext object.  (2) Next, the manager creates a set of one    or more rows in the ATM VC Cross Connect    Table, one for each cross\-connection between    two VCLs.  Each row is indexed by the ATM    interface port numbers and VPI/VCI values of    the two ends of that cross\-connection.    This set of rows specifies the topology of the    VCC cross\-connect and is identified by a single    value of atmVcCrossConnectIndex.  Negotiated VC Cross\-Connect Establishment  (2a) The manager creates a row in this table by    setting atmVcCrossConnectRowStatus to    createAndWait(5).  The agent checks the    requested topology and the mutual sanity of    the ATM traffic parameters and    service categories, i.e., the row creation    fails if\:    \- the requested topology is incompatible with      associated values of atmVclCastType,    \- the requested topology is not supported      by the agent,    \- the traffic/service category parameter values      associated with the requested row are      incompatible with those of already existing      rows for this VC cross\-connect.    [For example, for setting up    a point\-to\-point VC cross\-connect, the    ATM traffic parameters in the receive direction    of a VCL at the low end of the cross\-connect    must equal to the traffic parameters in the    transmit direction of the other VCL at the    high end of the cross\-connect,    otherwise, the row creation fails.]    The agent also checks for internal errors    in building the cross\-connect.     The atmVcCrossConnectIndex values in the    corresponding atmVclTable rows are filled    in by the agent at this point.  (2b) The manager promotes the row in the    atmVcCrossConnectTable by setting    atmVcCrossConnectRowStatus to active(1).  If    this set is successful, the agent has reserved    the resources specified by the ATM traffic    parameter and Service category values    for each direction of the VC cross\-connect    in an ATM switch or network.  (3) The manager sets the    atmVcCrossConnectAdminStatus to up(1)    in all rows of this VC cross\-connect to    turn the traffic flow on.   One\-Shot VC Cross\-Connect Establishment  A VC cross\-connect may also be established in one step by a set\-request with all necessary parameter values and atmVcCrossConnectRowStatus set to createAndGo(4).  In contrast to the negotiated VC cross\-connect establishment which allows for detailed error checking i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VC cross\-connect establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VC Cross\-Connect Retirement  A VC cross\-connect identified by a particular value of atmVcCrossConnectIndex is released by\:  (1) Setting atmVcCrossConnectRowStatus of all rows    identified by this value of    atmVcCrossConnectIndex to destroy(6).    The agent may release all    associated resources, and the    atmVcCrossConnectIndex values in the    corresponding atmVclTable row are removed.    Note that a situation when only a subset of    the associated rows are deleted corresponds    to a VC topology change.  (2) After deletion of the appropriate    atmVcCrossConnectEntries, the manager may    set atmVclRowStatus to destroy(6) the    associated VCLs.  The agent releases    the resources and removes the associated    rows in the atmVclTable.  VC Cross\-Connect Reconfiguration  At the discretion of the agent, a VC cross\-connect may be reconfigured by adding and/or deleting leafs to/from the VC topology as per the VC cross\-connect establishment/retirement procedures. Reconfiguration of traffic/service category parameter values requires release of the VC cross\-connect before those parameter values may by changed for individual VCLs
        	**type**\: list of  		 :py:class:`AtmVcCrossConnectEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.AtmVcCrossConnectTable, self).__init__()

            self.yang_name = "atmVcCrossConnectTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atmVcCrossConnectEntry", ("atmvccrossconnectentry", ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry))])
            self._leafs = OrderedDict()

            self.atmvccrossconnectentry = YList(self)
            self._segment_path = lambda: "atmVcCrossConnectTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.AtmVcCrossConnectTable, [], name, value)


        class AtmVcCrossConnectEntry(Entity):
            """
            An entry in the ATM VC Cross Connect table.
            This entry is used to model a bi\-directional ATM
            VC cross\-connect cross\-connecting two end points.
            
            Step\-wise Procedures to set up a VC Cross\-connect
            
            Once the entries in the atmVclTable are created,
            the following procedures are used
            to cross\-connect the VCLs together to
            form a VCC segment.
            
            (1) The manager obtains a unique
               atmVcCrossConnectIndex by reading the
               atmVcCrossConnectIndexNext object.
            
            (2) Next, the manager creates a set of one
               or more rows in the ATM VC Cross Connect
               Table, one for each cross\-connection between
               two VCLs.  Each row is indexed by the ATM
               interface port numbers and VPI/VCI values of
               the two ends of that cross\-connection.
               This set of rows specifies the topology of the
               VCC cross\-connect and is identified by a single
               value of atmVcCrossConnectIndex.
            
            Negotiated VC Cross\-Connect Establishment
            
            (2a) The manager creates a row in this table by
               setting atmVcCrossConnectRowStatus to
               createAndWait(5).  The agent checks the
               requested topology and the mutual sanity of
               the ATM traffic parameters and
               service categories, i.e., the row creation
               fails if\:
               \- the requested topology is incompatible with
                 associated values of atmVclCastType,
               \- the requested topology is not supported
                 by the agent,
               \- the traffic/service category parameter values
                 associated with the requested row are
                 incompatible with those of already existing
                 rows for this VC cross\-connect.
               [For example, for setting up
               a point\-to\-point VC cross\-connect, the
               ATM traffic parameters in the receive direction
               of a VCL at the low end of the cross\-connect
               must equal to the traffic parameters in the
               transmit direction of the other VCL at the
               high end of the cross\-connect,
               otherwise, the row creation fails.]
               The agent also checks for internal errors
               in building the cross\-connect.
            
               The atmVcCrossConnectIndex values in the
               corresponding atmVclTable rows are filled
               in by the agent at this point.
            
            (2b) The manager promotes the row in the
               atmVcCrossConnectTable by setting
               atmVcCrossConnectRowStatus to active(1).  If
               this set is successful, the agent has reserved
               the resources specified by the ATM traffic
               parameter and Service category values
               for each direction of the VC cross\-connect
               in an ATM switch or network.
            
            (3) The manager sets the
               atmVcCrossConnectAdminStatus to up(1)
               in all rows of this VC cross\-connect to
               turn the traffic flow on.
            
            
            One\-Shot VC Cross\-Connect Establishment
            
            A VC cross\-connect may also be established in
            one step by a set\-request with all necessary
            parameter values and atmVcCrossConnectRowStatus
            set to createAndGo(4).
            
            In contrast to the negotiated VC cross\-connect
            establishment which allows for detailed error
            checking i.e., set errors are explicitly linked to
            particular resource acquisition failures), the
            one\-shot VC cross\-connect establishment
            performs the setup on one operation but does
            not have the advantage of step\-wise error
            checking.
            
            VC Cross\-Connect Retirement
            
            A VC cross\-connect identified by a particular
            value of atmVcCrossConnectIndex is released by\:
            
            (1) Setting atmVcCrossConnectRowStatus of all rows
               identified by this value of
               atmVcCrossConnectIndex to destroy(6).
               The agent may release all
               associated resources, and the
               atmVcCrossConnectIndex values in the
               corresponding atmVclTable row are removed.
               Note that a situation when only a subset of
               the associated rows are deleted corresponds
               to a VC topology change.
            
            (2) After deletion of the appropriate
               atmVcCrossConnectEntries, the manager may
               set atmVclRowStatus to destroy(6) the
               associated VCLs.  The agent releases
               the resources and removes the associated
               rows in the atmVclTable.
            
            VC Cross\-Connect Reconfiguration
            
            At the discretion of the agent, a VC
            cross\-connect may be reconfigured by
            adding and/or deleting leafs to/from
            the VC topology as per the VC cross\-connect
            establishment/retirement procedures.
            Reconfiguration of traffic/service category parameter
            values requires release of the VC cross\-connect
            before those parameter values may by changed
            for individual VCLs.
            
            .. attribute:: atmvccrossconnectindex  (key)
            
            	A unique value to identify this VC cross\-connect. For each VCL associated with this cross\-connect, the agent reports this cross\-connect index value in the atmVclCrossConnectIdentifier attribute of the corresponding atmVclTable entries
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnectlowifindex  (key)
            
            	The ifIndex value of the ATM interface for this VC cross\-connect. The term low implies that this ATM interface has the numerically lower ifIndex value than the other ATM interface identified in the same atmVcCrossConnectEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnectlowvpi  (key)
            
            	The VPI value at the ATM interface associated with the VC cross\-connect that is identified by atmVcCrossConnectLowIfIndex
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnectlowvci  (key)
            
            	The VCI value at the ATM interface associated with this VC cross\-connect that is identified by atmVcCrossConnectLowIfIndex
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnecthighifindex  (key)
            
            	The ifIndex value for the ATM interface for this VC cross\-connect. The term high implies that this ATM interface has the numerically higher ifIndex value than the other ATM interface identified in the same atmVcCrossConnectEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnecthighvpi  (key)
            
            	The VPI value at the ATM interface associated with the VC cross\-connect that is identified by atmVcCrossConnectHighIfIndex
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnecthighvci  (key)
            
            	The VCI value at the ATM interface associated with the VC cross\-connect that is identified by atmVcCrossConnectHighIfIndex
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnectadminstatus
            
            	The desired administrative status of this bi\-directional VC cross\-connect
            	**type**\:  :py:class:`AtmVorXAdminStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnectl2hoperstatus
            
            	The current operational status of the VC cross\-connect in one direction; (i.e., from the low to high direction)
            	**type**\:  :py:class:`AtmVorXOperStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXOperStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnecth2loperstatus
            
            	The current operational status of the VC cross\-connect in one direction; (i.e., from the high to low direction)
            	**type**\:  :py:class:`AtmVorXOperStatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmVorXOperStatus>`
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnectl2hlastchange
            
            	The value of sysUpTime at the time this VC cross\-connect entered its current operational state in low to high direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnecth2llastchange
            
            	The value of sysUpTime at the time this VC cross\-connect entered its current operational state in high to low direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: atmvccrossconnectrowstatus
            
            	The status of this entry in the atmVcCrossConnectTable.  This object is used to create a new cross\-connect for cross\-connecting VCLs which are created using the atmVclTable or to change or delete existing cross\-connect. This object must be initially set to `createAndWait' or 'createAndGo'. To turn on a VC cross\-connect, the atmVcCrossConnectAdminStatus is set to `up'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry, self).__init__()

                self.yang_name = "atmVcCrossConnectEntry"
                self.yang_parent_name = "atmVcCrossConnectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['atmvccrossconnectindex','atmvccrossconnectlowifindex','atmvccrossconnectlowvpi','atmvccrossconnectlowvci','atmvccrossconnecthighifindex','atmvccrossconnecthighvpi','atmvccrossconnecthighvci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('atmvccrossconnectindex', (YLeaf(YType.int32, 'atmVcCrossConnectIndex'), ['int'])),
                    ('atmvccrossconnectlowifindex', (YLeaf(YType.int32, 'atmVcCrossConnectLowIfIndex'), ['int'])),
                    ('atmvccrossconnectlowvpi', (YLeaf(YType.int32, 'atmVcCrossConnectLowVpi'), ['int'])),
                    ('atmvccrossconnectlowvci', (YLeaf(YType.int32, 'atmVcCrossConnectLowVci'), ['int'])),
                    ('atmvccrossconnecthighifindex', (YLeaf(YType.int32, 'atmVcCrossConnectHighIfIndex'), ['int'])),
                    ('atmvccrossconnecthighvpi', (YLeaf(YType.int32, 'atmVcCrossConnectHighVpi'), ['int'])),
                    ('atmvccrossconnecthighvci', (YLeaf(YType.int32, 'atmVcCrossConnectHighVci'), ['int'])),
                    ('atmvccrossconnectadminstatus', (YLeaf(YType.enumeration, 'atmVcCrossConnectAdminStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXAdminStatus', '')])),
                    ('atmvccrossconnectl2hoperstatus', (YLeaf(YType.enumeration, 'atmVcCrossConnectL2HOperStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXOperStatus', '')])),
                    ('atmvccrossconnecth2loperstatus', (YLeaf(YType.enumeration, 'atmVcCrossConnectH2LOperStatus'), [('ydk.models.cisco_ios_xe.ATM_TC_MIB', 'AtmVorXOperStatus', '')])),
                    ('atmvccrossconnectl2hlastchange', (YLeaf(YType.uint32, 'atmVcCrossConnectL2HLastChange'), ['int'])),
                    ('atmvccrossconnecth2llastchange', (YLeaf(YType.uint32, 'atmVcCrossConnectH2LLastChange'), ['int'])),
                    ('atmvccrossconnectrowstatus', (YLeaf(YType.enumeration, 'atmVcCrossConnectRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.atmvccrossconnectindex = None
                self.atmvccrossconnectlowifindex = None
                self.atmvccrossconnectlowvpi = None
                self.atmvccrossconnectlowvci = None
                self.atmvccrossconnecthighifindex = None
                self.atmvccrossconnecthighvpi = None
                self.atmvccrossconnecthighvci = None
                self.atmvccrossconnectadminstatus = None
                self.atmvccrossconnectl2hoperstatus = None
                self.atmvccrossconnecth2loperstatus = None
                self.atmvccrossconnectl2hlastchange = None
                self.atmvccrossconnecth2llastchange = None
                self.atmvccrossconnectrowstatus = None
                self._segment_path = lambda: "atmVcCrossConnectEntry" + "[atmVcCrossConnectIndex='" + str(self.atmvccrossconnectindex) + "']" + "[atmVcCrossConnectLowIfIndex='" + str(self.atmvccrossconnectlowifindex) + "']" + "[atmVcCrossConnectLowVpi='" + str(self.atmvccrossconnectlowvpi) + "']" + "[atmVcCrossConnectLowVci='" + str(self.atmvccrossconnectlowvci) + "']" + "[atmVcCrossConnectHighIfIndex='" + str(self.atmvccrossconnecthighifindex) + "']" + "[atmVcCrossConnectHighVpi='" + str(self.atmvccrossconnecthighvpi) + "']" + "[atmVcCrossConnectHighVci='" + str(self.atmvccrossconnecthighvci) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/atmVcCrossConnectTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry, [u'atmvccrossconnectindex', u'atmvccrossconnectlowifindex', u'atmvccrossconnectlowvpi', u'atmvccrossconnectlowvci', u'atmvccrossconnecthighifindex', u'atmvccrossconnecthighvpi', u'atmvccrossconnecthighvci', u'atmvccrossconnectadminstatus', u'atmvccrossconnectl2hoperstatus', u'atmvccrossconnecth2loperstatus', u'atmvccrossconnectl2hlastchange', u'atmvccrossconnecth2llastchange', u'atmvccrossconnectrowstatus'], name, value)




    class Aal5VccTable(Entity):
        """
        This table contains AAL5 VCC performance
        parameters.
        
        .. attribute:: aal5vccentry
        
        	This list contains the AAL5 VCC performance parameters and is indexed by ifIndex values of AAL5 interfaces and the associated VPI/VCI values
        	**type**\: list of  		 :py:class:`Aal5VccEntry <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Aal5VccTable.Aal5VccEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(ATMMIB.Aal5VccTable, self).__init__()

            self.yang_name = "aal5VccTable"
            self.yang_parent_name = "ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("aal5VccEntry", ("aal5vccentry", ATMMIB.Aal5VccTable.Aal5VccEntry))])
            self._leafs = OrderedDict()

            self.aal5vccentry = YList(self)
            self._segment_path = lambda: "aal5VccTable"
            self._absolute_path = lambda: "ATM-MIB:ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ATMMIB.Aal5VccTable, [], name, value)


        class Aal5VccEntry(Entity):
            """
            This list contains the AAL5 VCC
            performance parameters and is indexed
            by ifIndex values of AAL5 interfaces
            and the associated VPI/VCI values.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: aal5vccvpi  (key)
            
            	The VPI value of the AAL5 VCC at the interface identified by the ifIndex
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: aal5vccvci  (key)
            
            	The VCI value of the AAL5 VCC at the interface identified by the ifIndex
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: aal5vcccrcerrors
            
            	The number of AAL5 CPCS PDUs received with CRC\-32 errors on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: aal5vccsartimeouts
            
            	The number of partially re\-assembled AAL5 CPCS PDUs which were discarded on this AAL5 VCC at the interface associated with an AAL5 entity because they were not fully re\-assembled within the required time period.  If the re\-assembly timer is not supported, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: aal5vccoversizedsdus
            
            	The number of AAL5 CPCS PDUs discarded on this AAL5 VCC at the interface associated with an AAL5 entity because the AAL5 SDUs were too large
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caal5vccinpkts
            
            	The number of AAL5 CPCS PDUs received on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: caal5vccoutpkts
            
            	The number of AAL5 CPCS PDUs transmitted on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: caal5vccinoctets
            
            	The number of AAL5 CPCS PDU octets received on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: caal5vccoutoctets
            
            	The number of AAL5 CPCS PDU octets transmitted on this AAL5  VCC at the interface associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: caal5vccindroppedpkts
            
            	The number of AAL5 CPCS PDUs dropped at the  receive side of this AAL5 VCC at the interface  associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: caal5vccoutdroppedpkts
            
            	The number of AAL5 CPCS PDUs dropped at the transmit side  of this AAL5 VCC at the interface associated with an  AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: caal5vccindroppedoctets
            
            	The number of AAL5 CPCS PDU Octets dropped at the  receive side of this AAL5 VCC at the interface  associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: caal5vccoutdroppedoctets
            
            	The number of AAL5 CPCS PDU Octets dropped at the  transmit side of this AAL5 VCC at the interface  associated with an AAL5 entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: caal5vcchcinpkts
            
            	This is 64bit (High Capacity) version of cAal5VccInPkts  counters
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: caal5vcchcoutpkts
            
            	This is 64bit (High Capacity) version of cAal5VccOutPkts  counters
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: caal5vcchcinoctets
            
            	This is 64bit (High Capacity) version of cAal5VccInOctets  counters
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: caal5vcchcoutoctets
            
            	This is 64bit (High Capacity) version of cAal5VccOutOctets  counters
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: caal5vccextcompenabled
            
            	Boolean, if compression enabled for VCC
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: caal5vccextvoice
            
            	Boolean, TRUE if VCC is used to carry voice
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: caal5vccextinf5oamcells
            
            	Number of OAM F5 end to end loopback cells  received through the VCC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caal5vccextoutf5oamcells
            
            	Number of OAM F5 end to end loopback cells sent  through the VCC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(ATMMIB.Aal5VccTable.Aal5VccEntry, self).__init__()

                self.yang_name = "aal5VccEntry"
                self.yang_parent_name = "aal5VccTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','aal5vccvpi','aal5vccvci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('aal5vccvpi', (YLeaf(YType.int32, 'aal5VccVpi'), ['int'])),
                    ('aal5vccvci', (YLeaf(YType.int32, 'aal5VccVci'), ['int'])),
                    ('aal5vcccrcerrors', (YLeaf(YType.uint32, 'aal5VccCrcErrors'), ['int'])),
                    ('aal5vccsartimeouts', (YLeaf(YType.uint32, 'aal5VccSarTimeOuts'), ['int'])),
                    ('aal5vccoversizedsdus', (YLeaf(YType.uint32, 'aal5VccOverSizedSDUs'), ['int'])),
                    ('caal5vccinpkts', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccInPkts'), ['int'])),
                    ('caal5vccoutpkts', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccOutPkts'), ['int'])),
                    ('caal5vccinoctets', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccInOctets'), ['int'])),
                    ('caal5vccoutoctets', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccOutOctets'), ['int'])),
                    ('caal5vccindroppedpkts', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccInDroppedPkts'), ['int'])),
                    ('caal5vccoutdroppedpkts', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccOutDroppedPkts'), ['int'])),
                    ('caal5vccindroppedoctets', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccInDroppedOctets'), ['int'])),
                    ('caal5vccoutdroppedoctets', (YLeaf(YType.uint32, 'CISCO-AAL5-MIB:cAal5VccOutDroppedOctets'), ['int'])),
                    ('caal5vcchcinpkts', (YLeaf(YType.uint64, 'CISCO-AAL5-MIB:cAal5VccHCInPkts'), ['int'])),
                    ('caal5vcchcoutpkts', (YLeaf(YType.uint64, 'CISCO-AAL5-MIB:cAal5VccHCOutPkts'), ['int'])),
                    ('caal5vcchcinoctets', (YLeaf(YType.uint64, 'CISCO-AAL5-MIB:cAal5VccHCInOctets'), ['int'])),
                    ('caal5vcchcoutoctets', (YLeaf(YType.uint64, 'CISCO-AAL5-MIB:cAal5VccHCOutOctets'), ['int'])),
                    ('caal5vccextcompenabled', (YLeaf(YType.boolean, 'CISCO-ATM-EXT-MIB:cAal5VccExtCompEnabled'), ['bool'])),
                    ('caal5vccextvoice', (YLeaf(YType.boolean, 'CISCO-ATM-EXT-MIB:cAal5VccExtVoice'), ['bool'])),
                    ('caal5vccextinf5oamcells', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:cAal5VccExtInF5OamCells'), ['int'])),
                    ('caal5vccextoutf5oamcells', (YLeaf(YType.uint32, 'CISCO-ATM-EXT-MIB:cAal5VccExtOutF5OamCells'), ['int'])),
                ])
                self.ifindex = None
                self.aal5vccvpi = None
                self.aal5vccvci = None
                self.aal5vcccrcerrors = None
                self.aal5vccsartimeouts = None
                self.aal5vccoversizedsdus = None
                self.caal5vccinpkts = None
                self.caal5vccoutpkts = None
                self.caal5vccinoctets = None
                self.caal5vccoutoctets = None
                self.caal5vccindroppedpkts = None
                self.caal5vccoutdroppedpkts = None
                self.caal5vccindroppedoctets = None
                self.caal5vccoutdroppedoctets = None
                self.caal5vcchcinpkts = None
                self.caal5vcchcoutpkts = None
                self.caal5vcchcinoctets = None
                self.caal5vcchcoutoctets = None
                self.caal5vccextcompenabled = None
                self.caal5vccextvoice = None
                self.caal5vccextinf5oamcells = None
                self.caal5vccextoutf5oamcells = None
                self._segment_path = lambda: "aal5VccEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[aal5VccVpi='" + str(self.aal5vccvpi) + "']" + "[aal5VccVci='" + str(self.aal5vccvci) + "']"
                self._absolute_path = lambda: "ATM-MIB:ATM-MIB/aal5VccTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ATMMIB.Aal5VccTable.Aal5VccEntry, [u'ifindex', u'aal5vccvpi', u'aal5vccvci', u'aal5vcccrcerrors', u'aal5vccsartimeouts', u'aal5vccoversizedsdus', 'caal5vccinpkts', 'caal5vccoutpkts', 'caal5vccinoctets', 'caal5vccoutoctets', 'caal5vccindroppedpkts', 'caal5vccoutdroppedpkts', 'caal5vccindroppedoctets', 'caal5vccoutdroppedoctets', 'caal5vcchcinpkts', 'caal5vcchcoutpkts', 'caal5vcchcinoctets', 'caal5vcchcoutoctets', 'caal5vccextcompenabled', 'caal5vccextvoice', 'caal5vccextinf5oamcells', 'caal5vccextoutf5oamcells'], name, value)



    def clone_ptr(self):
        self._top_entity = ATMMIB()
        return self._top_entity



